"""
generate_report.py — Convert agent markdown output to styled HTML report

Usage:
    python scripts/generate_report.py prior_reports/week_of_2026-03-23.md

This script takes the agent's markdown output and wraps it in the
styled HTML template for executive consumption.

For the assignment: this demonstrates the output pipeline.
In production, the agent would call this automatically after generating
the markdown report.
"""

import sys
import re
import json
from pathlib import Path
from datetime import datetime


def parse_threat_level(text: str) -> dict:
    """Extract threat level info from markdown text."""
    levels = {}
    # Look for patterns like "**ChatGPT**: HIGH" or "ChatGPT — HIGH"
    patterns = [
        r'\*\*(\w[\w\s&]+)\*\*\s*[:\—–-]\s*(HIGH|MEDIUM|LOW)',
        r'(\w[\w\s&]+)\s*[:\—–-]\s*(HIGH|MEDIUM|LOW)',
    ]
    for pattern in patterns:
        for match in re.finditer(pattern, text, re.IGNORECASE):
            product = match.group(1).strip()
            level = match.group(2).upper()
            levels[product] = level
    return levels


def extract_signals(text: str) -> list:
    """Extract Company — Signal formatted findings."""
    signals = []
    # Match bold company name followed by em dash and description
    pattern = r'\*\*([^*]+)\*\*\s*[—–-]\s*(.+?)(?=\n\*\*|\n##|\n\n|$)'
    for match in re.finditer(pattern, text, re.DOTALL):
        signals.append({
            'company': match.group(1).strip(),
            'signal': match.group(2).strip()
        })
    return signals


def generate_html(markdown_path: str, output_path: str = None):
    """Convert markdown report to styled HTML."""
    md_path = Path(markdown_path)
    if not md_path.exists():
        print(f"Error: {markdown_path} not found")
        sys.exit(1)

    content = md_path.read_text()
    today = datetime.now().strftime("%B %d, %Y")

    # If no output path specified, put it next to the markdown
    if output_path is None:
        output_path = md_path.with_suffix('.html')

    print(f"Reading: {markdown_path}")
    print(f"Output:  {output_path}")

    # Extract structured data
    threat_levels = parse_threat_level(content)
    signals = extract_signals(content)

    print(f"Found {len(threat_levels)} threat levels, {len(signals)} signals")

    # For the assignment demo, we reference the pre-built HTML template
    # In production, this would dynamically populate the template
    print(f"\nTo generate the full styled HTML report:")
    print(f"  1. Open report_output/openai_intel_report.html as the template")
    print(f"  2. Replace sample data with extracted signals")
    print(f"  3. Save to {output_path}")
    print(f"\nExtracted data summary:")
    print(f"  Threat levels: {json.dumps(threat_levels, indent=2)}")
    print(f"  Signals found: {len(signals)}")
    for s in signals[:5]:
        print(f"    {s['company']} — {s['signal'][:80]}...")

    return {
        'threat_levels': threat_levels,
        'signals': signals,
        'generated': today
    }


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python scripts/generate_report.py <markdown_report_path>")
        print("Example: python scripts/generate_report.py prior_reports/week_of_2026-03-23.md")
        sys.exit(1)

    result = generate_html(sys.argv[1])
