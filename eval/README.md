# Evaluation Framework

> **Owners**: Tatsuro & Ez
> **Status**: Scaffolded — ready for your input

## Suggested Approach

Based on our team discussion, the evaluation agent should:

1. **Define 10 test scenarios** — competitive situations with known-correct answers
2. **Feed each scenario to the intelligence agent** as if it were real data
3. **Score the agent's output** against the correct answers using another LLM as a grader

## Scoring Dimensions

| Dimension | What to measure | Weight |
|-----------|----------------|--------|
| Signal detection | Did the agent find the key competitive signal? | 30% |
| Product-line classification | Did it route the signal to the right section (ChatGPT/Codex/API)? | 20% |
| Threat-level accuracy | Is the HIGH/MEDIUM/LOW rating appropriate? | 20% |
| Source citation | Did it cite real sources, not fabricate? | 15% |
| Actionability | Is the "So What?" implication useful for a decision-maker? | 15% |

## Example Test Scenario

```json
{
  "scenario_id": 1,
  "description": "Anthropic releases a new model that beats GPT-4o on SWE-Bench",
  "simulated_signals": [
    "Anthropic blog post: Claude Sonnet 4.6 achieves 55% on SWE-Bench Verified",
    "Hacker News thread with 500+ upvotes discussing the results",
    "Two developer tweets comparing Claude Code vs Codex"
  ],
  "expected_output": {
    "product_line": "Codex",
    "threat_level": "HIGH",
    "confidence": "HIGH",
    "should_mention": ["SWE-Bench", "Claude Code", "benchmark"]
  }
}
```

## File Structure

```
eval/
├── README.md              ← You are here
├── test_scenarios.json    ← 10 test cases (you create this)
├── run_eval.py            ← Script to run eval (you create this)
└── eval_results.md        ← Results and analysis (you create this)
```

## Output Schema Reference

The intelligence agent's output follows the schema in `SUBMISSION.md` Section 5.
The key fields to evaluate against:

- `c_suite_dashboard.threat_levels.{product}.level` — HIGH/MEDIUM/LOW
- `c_suite_dashboard.threat_levels.{product}.confidence` — HIGH/MEDIUM/LOW
- `c_suite_dashboard.must_know_this_week[].signal` — one-line descriptions
- `{section}_intelligence.{subsection}[]` — individual findings

## How to Run (once you build it)

```bash
python eval/run_eval.py --scenarios eval/test_scenarios.json --output eval/eval_results.md
```
