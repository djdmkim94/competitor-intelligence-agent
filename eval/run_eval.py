"""
run_eval.py — Evaluate the agent's report output using LLM-as-judge

Usage:
    python eval/run_eval.py --report prior_reports/week_of_2026-03-23.md
    python eval/run_eval.py --report prior_reports/week_of_2026-03-23.md --output eval/eval_results.md

Loads 10 test scenarios from eval/test_scenarios.json, checks the agent's
real report output against each scenario's expected results, and uses
Claude as a judge to score on 5 dimensions.
"""

import json
import sys
import os
import re
from pathlib import Path
from datetime import datetime

try:
    import anthropic
    HAS_ANTHROPIC = True
except ImportError:
    HAS_ANTHROPIC = False

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


SCORING_DIMENSIONS = {
    "signal_detection": {
        "weight": 0.30,
        "description": "Did the agent find and include the key competitive signal?",
    },
    "product_line_classification": {
        "weight": 0.20,
        "description": "Did the agent route the signal to the correct report section?",
    },
    "threat_level_accuracy": {
        "weight": 0.20,
        "description": "Is the HIGH/MEDIUM/LOW threat level appropriate for this signal?",
    },
    "source_citation": {
        "weight": 0.15,
        "description": "Did the agent cite real sources? Are the sources relevant and not fabricated?",
    },
    "actionability": {
        "weight": 0.15,
        "description": "Is the 'So What?' implication useful for a decision-maker?",
    },
}

JUDGE_PROMPT = """You are an expert evaluator for a competitive intelligence agent. You will be given:

1. A TEST SCENARIO describing a real competitive signal with ground truth sources
2. The AGENT'S REPORT output (a weekly competitive intelligence report)
3. EXPECTED RESULTS (what the agent should have detected)

Score the agent's handling of this scenario on 5 dimensions, each from 0-10:

1. **Signal Detection** (weight: 30%): Did the agent find and include this signal? 10 = signal clearly present with accurate details. 0 = signal completely missing.

2. **Product-Line Classification** (weight: 20%): Did the agent place this signal in the correct product-line section? 10 = correctly routed. 5 = mentioned but in wrong section. 0 = not mentioned.

3. **Threat-Level Accuracy** (weight: 20%): Is the agent's threat level rating appropriate? 10 = matches expected level. 7 = one level off but defensible. 3 = significantly wrong. Use the expected threat level as ground truth.

4. **Source Citation** (weight: 15%): Did the agent cite real, relevant sources for this signal? 10 = multiple real sources cited. 5 = one source or vague attribution. 0 = no sources or fabricated sources.

5. **Actionability** (weight: 15%): Is the implication/analysis useful for a decision-maker? 10 = specific, actionable insight. 5 = generic observation. 0 = no analysis or misleading.

Respond in this exact JSON format:
{
  "signal_detection": {"score": N, "reasoning": "..."},
  "product_line_classification": {"score": N, "reasoning": "..."},
  "threat_level_accuracy": {"score": N, "reasoning": "..."},
  "source_citation": {"score": N, "reasoning": "..."},
  "actionability": {"score": N, "reasoning": "..."},
  "keywords_found": ["list of expected keywords that WERE found in the report"],
  "keywords_missing": ["list of expected keywords that were NOT found"],
  "overall_notes": "Any additional observations about the agent's handling of this scenario"
}

Only output the JSON. No other text."""


def check_keywords(report_text: str, expected: dict) -> tuple:
    """Check which expected keywords are present/missing in the report."""
    report_lower = report_text.lower()
    found = []
    missing = []
    for kw in expected.get("should_mention", []):
        if kw.lower() in report_lower:
            found.append(kw)
        else:
            missing.append(kw)
    return found, missing


def judge_scenario(client, scenario: dict, report_text: str, use_openrouter: bool = False) -> dict:
    """Use Claude to judge the agent's output for one scenario."""
    user_msg = f"""## TEST SCENARIO
**Name**: {scenario['name']}
**Description**: {scenario['description']}
**Ground Truth Sources**: {json.dumps(scenario['ground_truth_sources'])}

## EXPECTED RESULTS
- Signal should be detected: {scenario['expected']['signal_detected']}
- Expected product line: {scenario['expected']['product_line']}
- Expected threat level: {scenario['expected']['threat_level']}
- Expected confidence: {scenario['expected']['confidence']}
- Should mention these keywords: {json.dumps(scenario['expected']['should_mention'])}

## AGENT'S REPORT OUTPUT
{report_text}"""

    if use_openrouter:
        api_key = os.environ.get("OPENROUTER_API_KEY", "")
        resp = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
            json={
                "model": "anthropic/claude-sonnet-4",
                "max_tokens": 1024,
                "messages": [{"role": "user", "content": JUDGE_PROMPT + "\n\n" + user_msg}],
            },
            timeout=120,
        )
        resp.raise_for_status()
        response_text = resp.json()["choices"][0]["message"]["content"].strip()
    else:
        response = client.messages.create(
            model="claude-sonnet-4-5-20241022",
            max_tokens=1024,
            messages=[{"role": "user", "content": JUDGE_PROMPT + "\n\n" + user_msg}],
        )
        response_text = response.content[0].text.strip()
    # Handle potential markdown code blocks
    if response_text.startswith("```"):
        response_text = re.sub(r"^```(?:json)?\n?", "", response_text)
        response_text = re.sub(r"\n?```$", "", response_text)

    try:
        return json.loads(response_text)
    except json.JSONDecodeError:
        return {
            "signal_detection": {"score": 0, "reasoning": "Judge response parse error"},
            "product_line_classification": {"score": 0, "reasoning": "Parse error"},
            "threat_level_accuracy": {"score": 0, "reasoning": "Parse error"},
            "source_citation": {"score": 0, "reasoning": "Parse error"},
            "actionability": {"score": 0, "reasoning": "Parse error"},
            "overall_notes": f"Raw judge response: {response_text[:500]}",
        }


def compute_weighted_score(result: dict) -> float:
    """Compute weighted score from dimension scores."""
    total = 0
    for dim, config in SCORING_DIMENSIONS.items():
        score = result.get(dim, {}).get("score", 0)
        total += score * config["weight"]
    return round(total, 2)


def generate_report(scenarios: list, results: list, report_path: str) -> str:
    """Generate the eval results markdown report."""
    today = datetime.now().strftime("%Y-%m-%d")

    lines = [
        "# Evaluation Results — Competitive Intelligence Agent",
        "",
        f"**Date**: {today}",
        f"**Report evaluated**: `{report_path}`",
        f"**Judge model**: Claude Sonnet 4.5",
        f"**Scenarios**: {len(scenarios)}",
        "",
        "## Scoring Dimensions",
        "",
        "| Dimension | Weight | Description |",
        "|-----------|--------|-------------|",
    ]
    for dim, config in SCORING_DIMENSIONS.items():
        lines.append(f"| {dim.replace('_', ' ').title()} | {int(config['weight']*100)}% | {config['description']} |")

    lines.extend(["", "---", "", "## Summary Scores", ""])
    lines.append("| # | Scenario | Weighted Score | Signal | Classification | Threat Level | Citation | Actionability |")
    lines.append("|---|----------|---------------|--------|----------------|-------------|----------|---------------|")

    total_weighted = 0
    for scenario, result in zip(scenarios, results):
        ws = compute_weighted_score(result)
        total_weighted += ws
        sd = result.get("signal_detection", {}).get("score", "?")
        pc = result.get("product_line_classification", {}).get("score", "?")
        tl = result.get("threat_level_accuracy", {}).get("score", "?")
        sc = result.get("source_citation", {}).get("score", "?")
        ac = result.get("actionability", {}).get("score", "?")
        lines.append(f"| {scenario['scenario_id']} | {scenario['name']} | **{ws}/10** | {sd} | {pc} | {tl} | {sc} | {ac} |")

    avg = round(total_weighted / len(scenarios), 2) if scenarios else 0
    lines.extend([
        "",
        f"**Overall Average**: **{avg}/10**",
        "",
        "---",
        "",
        "## Detailed Results",
    ])

    for scenario, result in zip(scenarios, results):
        ws = compute_weighted_score(result)
        lines.extend([
            "",
            f"### Scenario {scenario['scenario_id']}: {scenario['name']}",
            "",
            f"**Weighted Score**: {ws}/10",
            "",
            f"**Description**: {scenario['description']}",
            "",
            f"**Expected**: {scenario['expected']['product_line'].upper()} section, "
            f"Threat Level {scenario['expected']['threat_level']}, "
            f"Confidence {scenario['expected']['confidence']}",
            "",
            "| Dimension | Score | Reasoning |",
            "|-----------|-------|-----------|",
        ])

        for dim in SCORING_DIMENSIONS:
            d = result.get(dim, {})
            score = d.get("score", "?")
            reasoning = d.get("reasoning", "N/A").replace("|", "/").replace("\n", " ")
            lines.append(f"| {dim.replace('_', ' ').title()} | {score}/10 | {reasoning} |")

        kw_found = result.get("keywords_found", [])
        kw_missing = result.get("keywords_missing", [])
        notes = result.get("overall_notes", "")

        lines.extend([
            "",
            f"**Keywords found**: {', '.join(kw_found) if kw_found else 'N/A'}",
            f"**Keywords missing**: {', '.join(kw_missing) if kw_missing else 'None'}",
            f"**Judge notes**: {notes}",
        ])

    lines.extend([
        "",
        "---",
        "",
        f"*Evaluation generated {today} by run_eval.py using Claude Sonnet 4.5 as judge*",
    ])

    return "\n".join(lines)


def main():
    report_path = "prior_reports/week_of_2026-03-23.md"
    output_path = "eval/eval_results.md"

    if "--report" in sys.argv:
        idx = sys.argv.index("--report")
        if idx + 1 < len(sys.argv):
            report_path = sys.argv[idx + 1]

    if "--output" in sys.argv:
        idx = sys.argv.index("--output")
        if idx + 1 < len(sys.argv):
            output_path = sys.argv[idx + 1]

    # Load report
    report_file = Path(report_path)
    if not report_file.exists():
        print(f"Error: Report not found at {report_path}")
        sys.exit(1)
    report_text = report_file.read_text()

    # Load scenarios
    scenarios_file = Path("eval/test_scenarios.json")
    if not scenarios_file.exists():
        print("Error: eval/test_scenarios.json not found")
        sys.exit(1)
    scenarios = json.loads(scenarios_file.read_text())

    print(f"Evaluating {len(scenarios)} scenarios against {report_path}")
    print(f"Judge model: Claude Sonnet 4.5")
    print()

    # Init API client — try Anthropic first, fall back to OpenRouter
    use_openrouter = False
    client = None
    anthropic_key = os.environ.get("ANTHROPIC_API_KEY")
    openrouter_key = os.environ.get("OPENROUTER_API_KEY")

    if anthropic_key and HAS_ANTHROPIC:
        client = anthropic.Anthropic(api_key=anthropic_key)
        print("Using Anthropic API directly")
    elif openrouter_key:
        use_openrouter = True
        print("Using OpenRouter API (Claude via OpenRouter)")
    else:
        print("Error: Set ANTHROPIC_API_KEY or OPENROUTER_API_KEY")
        sys.exit(1)

    # Run evaluation
    results = []
    for scenario in scenarios:
        print(f"  [{scenario['scenario_id']}/10] {scenario['name']}...", end=" ", flush=True)

        # Pre-check keywords
        kw_found, kw_missing = check_keywords(report_text, scenario["expected"])

        # Judge with LLM (with retry on timeout)
        result = None
        for attempt in range(3):
            try:
                result = judge_scenario(client, scenario, report_text, use_openrouter=use_openrouter)
                break
            except Exception as e:
                if attempt < 2:
                    print(f"retry {attempt+1}...", end=" ", flush=True)
                else:
                    print(f"FAILED ({e})")
                    result = {
                        "signal_detection": {"score": 0, "reasoning": f"Judge error: {str(e)[:100]}"},
                        "product_line_classification": {"score": 0, "reasoning": "Error"},
                        "threat_level_accuracy": {"score": 0, "reasoning": "Error"},
                        "source_citation": {"score": 0, "reasoning": "Error"},
                        "actionability": {"score": 0, "reasoning": "Error"},
                        "overall_notes": f"Judge failed after 3 attempts: {str(e)[:200]}",
                    }

        # Merge keyword check
        if "keywords_found" not in result:
            result["keywords_found"] = kw_found
        if "keywords_missing" not in result:
            result["keywords_missing"] = kw_missing

        ws = compute_weighted_score(result)
        print(f"{ws}/10")
        results.append(result)

    # Generate report
    avg = round(sum(compute_weighted_score(r) for r in results) / len(results), 2)
    print(f"\nOverall Average: {avg}/10")
    print()

    md = generate_report(scenarios, results, report_path)
    Path(output_path).write_text(md)
    print(f"Results saved to {output_path}")


if __name__ == "__main__":
    main()
