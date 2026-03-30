"""
exa_scan.py — Run Exa semantic search across all competitor product lines

Usage:
    python scripts/exa_scan.py                     # Full scan, save to prior_reports/
    python scripts/exa_scan.py --days 3             # Look back 3 days (default: 7)
    python scripts/exa_scan.py --section codex      # Scan only one section
    python scripts/exa_scan.py --json               # Output raw JSON

Runs semantic searches via Exa API for each competitor in each product line,
aggregates results, and saves a structured markdown file for the agent to
incorporate into its weekly report.
"""

import sys
import json
import os
from datetime import datetime, timedelta
from pathlib import Path


# Exa API key — must be set as environment variable
EXA_API_KEY = os.environ.get("EXA_API_KEY", "")
if not EXA_API_KEY:
    print("ERROR: EXA_API_KEY not set. Run: export EXA_API_KEY=your_key")
    sys.exit(1)

# Queries organized by product line
SCAN_QUERIES = {
    "ChatGPT (Consumer)": [
        "Anthropic Claude consumer product launch announcement",
        "Google Gemini consumer AI features update",
        "xAI Grok product announcement",
        "Perplexity AI product launch news",
    ],
    "Codex (Coding Tools)": [
        "Cursor AI coding tool Anysphere news funding",
        "Claude Code Anthropic developer tools update",
        "Google Gemini Code Assist Jules coding agent",
        "Cognition Devin Windsurf AI coding agent",
        "GitHub Copilot AI coding update",
    ],
    "API & Models (Platform)": [
        "DeepSeek AI model release benchmark",
        "Qwen Alibaba open source AI model release",
        "Zhipu AI GLM open source model",
        "Moonshot AI Kimi model update",
        "MiniMax AI model release",
        "open source LLM benchmark leaderboard 2026",
        "Chinese AI model market share OpenRouter",
    ],
    "Hiring & Resource Signals": [
        "Anthropic careers hiring AI engineer",
        "Google DeepMind Gemini hiring jobs",
        "Cursor Anysphere hiring engineering",
        "Cognition AI Devin hiring jobs",
        "AI startup hiring enterprise sales growth",
    ],
    "Horizon Watch": [
        "AI video generation model Sora competitor",
        "AI agent framework LangChain CrewAI 2026",
        "robotics AI convergence Figure Boston Dynamics",
    ],
}


def run_scan(days_back: int = 7, section_filter: str = None) -> dict:
    """Run Exa searches across all product lines."""
    from exa_py import Exa

    exa = Exa(EXA_API_KEY)
    start_date = (datetime.now() - timedelta(days=days_back)).strftime("%Y-%m-%d")
    results = {}

    for section, queries in SCAN_QUERIES.items():
        if section_filter and section_filter.lower() not in section.lower():
            continue

        results[section] = []
        print(f"\n{'='*60}")
        print(f"  {section}")
        print(f"{'='*60}")

        for query in queries:
            try:
                search_results = exa.search_and_contents(
                    query,
                    num_results=5,
                    start_published_date=start_date,
                    text={"max_characters": 300},
                )
                for r in search_results.results:
                    signal = {
                        "title": r.title or "",
                        "url": r.url,
                        "text": (r.text or "")[:300],
                        "published_date": getattr(r, "published_date", ""),
                        "query": query,
                        "section": section,
                    }
                    results[section].append(signal)
                    print(f"  + {r.title[:70] if r.title else 'No title'}")

            except Exception as e:
                print(f"  ! Error on '{query[:40]}': {e}")

        # Deduplicate by URL within section
        seen_urls = set()
        deduped = []
        for s in results[section]:
            if s["url"] not in seen_urls:
                seen_urls.add(s["url"])
                deduped.append(s)
        results[section] = deduped
        print(f"  → {len(deduped)} unique signals")

    return results


def results_to_markdown(results: dict, days_back: int) -> str:
    """Convert scan results to markdown for agent consumption."""
    today = datetime.now().strftime("%Y-%m-%d")
    start = (datetime.now() - timedelta(days=days_back)).strftime("%Y-%m-%d")

    lines = [
        f"# Exa Intelligence Scan",
        f"",
        f"**Period**: {start} to {today}",
        f"**Generated**: {today}",
        f"**Source**: Exa semantic search (exa.ai)",
        f"",
        f"---",
    ]

    total_signals = 0
    for section, signals in results.items():
        lines.append(f"\n## {section}\n")
        if not signals:
            lines.append("No significant signals detected.\n")
            continue

        for s in signals:
            title = s["title"] or "Untitled"
            lines.append(f"### {title}")
            lines.append(f"- **URL**: {s['url']}")
            if s.get("published_date"):
                lines.append(f"- **Published**: {s['published_date']}")
            if s.get("text"):
                lines.append(f"- **Excerpt**: {s['text'][:200]}...")
            lines.append("")
            total_signals += 1

    lines.append(f"\n---\n*{total_signals} total signals across {len(results)} sections*\n")
    return "\n".join(lines)


def main():
    days_back = 7
    section_filter = None
    output_json = "--json" in sys.argv

    if "--days" in sys.argv:
        idx = sys.argv.index("--days")
        if idx + 1 < len(sys.argv):
            days_back = int(sys.argv[idx + 1])

    if "--section" in sys.argv:
        idx = sys.argv.index("--section")
        if idx + 1 < len(sys.argv):
            section_filter = sys.argv[idx + 1]

    print(f"Exa Intelligence Scan")
    print(f"  Period: last {days_back} days")
    print(f"  Sections: {section_filter or 'all'}")

    results = run_scan(days_back=days_back, section_filter=section_filter)

    if output_json:
        print(json.dumps(results, indent=2, default=str))
    else:
        md = results_to_markdown(results, days_back)
        # Save to prior_reports/
        today = datetime.now().strftime("%Y-%m-%d")
        output_path = Path("prior_reports") / f"exa_scan_{today}.md"
        output_path.write_text(md)
        print(f"\n{'='*60}")
        print(f"  Saved to {output_path}")
        print(f"{'='*60}")

    total = sum(len(v) for v in results.values())
    print(f"\nDone! {total} unique signals found.")


if __name__ == "__main__":
    main()
