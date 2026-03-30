"""
generate_report.py — Convert agent markdown output to styled HTML report

Usage:
    python scripts/generate_report.py prior_reports/week_of_2026-03-23.md
    python scripts/generate_report.py prior_reports/week_of_2026-03-23.md -o report_output/report.html

Takes the agent's markdown output and generates a styled HTML dashboard
using the template structure from report_output/openai_intel_report.html.
"""

import sys
import re
import html
from pathlib import Path
from datetime import datetime


def escape(text: str) -> str:
    """HTML-escape text while preserving intentional bold markers."""
    return html.escape(text)


def parse_report(content: str) -> dict:
    """Parse the agent's markdown report into structured sections."""
    report = {
        "week_of": "",
        "generated": datetime.now().strftime("%B %d, %Y"),
        "threat_levels": {},
        "must_know": [],
        "chatgpt_signals": [],
        "codex_signals": [],
        "api_signals": [],
        "horizon_signals": [],
        "hiring_signals": [],
        "sources": [],
    }

    # Extract week/date from header
    week_match = re.search(r"Week of (.+?)(?:\n|,|$)", content)
    if week_match:
        report["week_of"] = week_match.group(1).strip()

    date_match = re.search(r"[Gg]enerated (?:on )?(.+?)(?:\n|$)", content)
    if date_match:
        report["generated"] = date_match.group(1).strip()

    # Extract threat levels from C-Suite Dashboard
    # Handles: | **ChatGPT** | HIGH | ●●● | ..., | ChatGPT | HIGH | HIGH |, **ChatGPT**: HIGH, etc.
    threat_patterns = [
        # Table with bold product name and confidence dots or text
        r"\|\s*\*\*(\w[\w\s&/]+?)\*\*\s*\|\s*(HIGH|MEDIUM|LOW|RED|YELLOW|GREEN)\s*\|\s*(●+○*|HIGH|MEDIUM|LOW)\s*\|",
        # Table without bold
        r"\|\s*(\w[\w\s&/]+?)\s*\|\s*(HIGH|MEDIUM|LOW|RED|YELLOW|GREEN)\s*\|\s*(●+○*|HIGH|MEDIUM|LOW)\s*\|",
        # Non-table format: **Product**: LEVEL or **Product** — LEVEL
        r"\*\*(\w[\w\s&/]+?)\*\*\s*[:\—–-]\s*(HIGH|MEDIUM|LOW|RED|YELLOW|GREEN)",
    ]
    for pattern in threat_patterns:
        for match in re.finditer(pattern, content, re.IGNORECASE):
            groups = match.groups()
            product = groups[0].strip()
            level = groups[1].upper()
            # Normalize RED/YELLOW/GREEN to HIGH/MEDIUM/LOW
            level_map = {"RED": "HIGH", "YELLOW": "MEDIUM", "GREEN": "LOW"}
            level = level_map.get(level, level)
            # Parse confidence from dots or text
            if len(groups) > 2:
                conf_raw = groups[2]
                if "●" in conf_raw:
                    filled = conf_raw.count("●")
                    confidence = {3: "HIGH", 2: "MEDIUM", 1: "LOW"}.get(filled, "MEDIUM")
                else:
                    confidence = conf_raw.upper()
            else:
                confidence = "MEDIUM"
            report["threat_levels"][product] = {
                "level": level,
                "confidence": confidence,
            }

    # Extract Must Know items
    # Handles multi-line numbered items: "1. **Company** — signal ... \n\n2. ..."
    must_know_match = re.search(
        r"Must Know.*?\n\n([\s\S]+?)(?=\n---|\n## )", content, re.IGNORECASE
    )
    if must_know_match:
        block = must_know_match.group(1)
        # Split by numbered items (1. 2. 3.)
        items = re.split(r"\n\d+\.\s+", "\n" + block)
        items = [item.strip() for item in items if item.strip()]
        # Take first line of each item for the summary
        report["must_know"] = [item.split("\n")[0] for item in items[:3]]

    # Extract signals per section using **Company** — Signal pattern
    def extract_signals(section_text: str) -> list:
        signals = []
        pattern = r"\*\*([^*]+)\*\*\s*[—–-]\s*(.+?)(?=\n\*\*|\n##|\n\n|$)"
        for match in re.finditer(pattern, section_text, re.DOTALL):
            signal_text = match.group(2).strip()
            # Split into headline and body if there's a newline
            parts = signal_text.split("\n", 1)
            headline = parts[0].strip()
            body = parts[1].strip() if len(parts) > 1 else ""
            # Extract source URLs
            sources = re.findall(r"https?://[^\s)]+", body or headline)
            signals.append({
                "company": match.group(1).strip(),
                "headline": headline,
                "body": body,
                "sources": sources,
            })
        return signals

    # Split content by major sections — match on HEADER LINE ONLY (first line)
    sections = re.split(r"^##\s+", content, flags=re.MULTILINE)
    for section in sections:
        header = section.split("\n")[0].lower()
        if "chatgpt" in header:
            report["chatgpt_signals"] = extract_signals(section)
        elif "codex" in header:
            report["codex_signals"] = extract_signals(section)
        elif "api" in header or ("model" in header and "intelligence" in header):
            report["api_signals"] = extract_signals(section)
        elif "horizon" in header:
            report["horizon_signals"] = extract_signals(section)
        elif "hiring" in header:
            report["hiring_signals"] = extract_signals(section)
        elif "source" in header:
            urls = re.findall(r"https?://[^\s)]+", section)
            report["sources"] = urls

    return report


def confidence_dots(level: str) -> str:
    """Generate confidence dot HTML."""
    filled = {"HIGH": 3, "MEDIUM": 2, "LOW": 1}.get(level.upper(), 2)
    dots = []
    for i in range(3):
        cls = "confidence-dot filled" if i < filled else "confidence-dot"
        dots.append(f'<span class="{cls}"></span>')
    return "".join(dots)


def threat_badge_class(level: str) -> str:
    """Map threat level to CSS class."""
    return {"HIGH": "high", "MEDIUM": "medium", "LOW": "low"}.get(level.upper(), "medium")


def product_tag_class(product: str) -> str:
    """Map product line to tag CSS class."""
    p = product.lower()
    if "chatgpt" in p or "consumer" in p:
        return "tag-chatgpt"
    elif "codex" in p or "coding" in p:
        return "tag-codex"
    else:
        return "tag-api"


def signal_card_html(signal: dict) -> str:
    """Generate a signal card HTML block."""
    company = escape(signal["company"])
    headline = escape(signal["headline"])
    body = escape(signal.get("body", ""))
    sources_html = ""
    if signal.get("sources"):
        links = [f'<a href="{s}">{s.split("//")[1].split("/")[0]}</a>' for s in signal["sources"][:3]]
        sources_html = f'<div class="source">Source: {" · ".join(links)}</div>'
    body_html = f"<p>{body}</p>" if body else ""
    return f"""      <div class="signal-card">
        <h4><span class="company-name">{company}</span> — {headline}</h4>
        {body_html}
        {sources_html}
      </div>"""


def generate_html(report: dict) -> str:
    """Generate the full HTML report from parsed data."""

    # --- Threat cards ---
    threat_cards = []
    product_labels = {
        "ChatGPT": ("Consumer", "chatgpt"),
        "Codex": ("Enterprise", "codex"),
        "API": ("Platform", "api"),
        "API & Models": ("Platform", "api"),
        "API/Models": ("Platform", "api"),
    }
    for product, info in report["threat_levels"].items():
        sub, _ = product_labels.get(product, ("Platform", "api"))
        badge_cls = threat_badge_class(info["level"])
        dots = confidence_dots(info.get("confidence", "MEDIUM"))
        threat_cards.append(f"""    <div class="threat-card">
      <div class="threat-card-header">
        <div><span class="product-name">{escape(product)}</span><span class="product-sub">{sub}</span></div>
        <span class="threat-level-badge {badge_cls}">{info["level"].title()}</span>
      </div>
      <div class="threat-card-body">
        <div class="confidence-line">
          <span class="confidence-label">Confidence</span>
          <span class="confidence-dots">{dots}</span>
        </div>
      </div>
    </div>""")

    # --- Must Know ---
    must_know_items = []
    for i, item in enumerate(report["must_know"][:3], 1):
        # Try to extract company name from bold markers
        company_match = re.match(r"\*\*([^*]+)\*\*\s*[—–-]\s*(.*)", item)
        if company_match:
            company = escape(company_match.group(1))
            text = escape(company_match.group(2))
            display = f'<span class="company-name">{company}</span> — {text}'
        else:
            display = escape(item)
        must_know_items.append(f"""      <li>
        <span class="num">{i:02d}</span>
        <span>{display}</span>
      </li>""")

    # --- Tab content ---
    def section_html(signals: list, section_title: str, section_desc: str) -> str:
        if not signals:
            return f"""    <div class="section">
      <h3>{section_title}</h3>
      <div class="section-desc">{section_desc}</div>
      <div class="signal-card"><p>No significant signals detected this week.</p></div>
    </div>"""
        cards = "\n".join(signal_card_html(s) for s in signals)
        return f"""    <div class="section">
      <h3>{section_title}</h3>
      <div class="section-desc">{section_desc}</div>
{cards}
    </div>"""

    chatgpt_content = section_html(
        report["chatgpt_signals"],
        "Competitive signals",
        "Messaging, sentiment, and marketing signals from consumer AI competitors",
    )
    codex_content = section_html(
        report["codex_signals"],
        "Competitive signals",
        "Feature launches, benchmarks, and enterprise signals from coding tool competitors",
    )
    api_content = section_html(
        report["api_signals"],
        "Competitive signals",
        "Model releases, pricing changes, partnerships, and open-source ecosystem shifts",
    )
    horizon_content = section_html(
        report["horizon_signals"],
        "Horizon Watch",
        "Rising challengers and emerging technologies",
    )

    # --- Sources ---
    sources_html = "<br>".join(escape(s) for s in report["sources"])

    # --- Full HTML ---
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>OpenAI Competitive Intelligence Report — {escape(report["week_of"])}</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=DM+Serif+Display&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
:root {{
  --bg: #FAFAF8; --surface: #FFFFFF; --surface-alt: #F5F4F0;
  --text: #1A1A18; --text-secondary: #6B6A65; --text-tertiary: #9C9A92;
  --border: #E8E7E2; --border-light: #F0EFEA; --accent: #1D1D1B;
  --blue-text: #1E40AF;
  --font: 'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-serif: 'DM Serif Display', Georgia, serif;
  --font-mono: 'JetBrains Mono', monospace;
}}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: var(--font); background: var(--bg); color: var(--text); line-height: 1.6; -webkit-font-smoothing: antialiased; }}
.container {{ max-width: 1080px; margin: 0 auto; padding: 48px 32px; }}
.report-header {{ margin-bottom: 48px; padding-bottom: 32px; border-bottom: 1px solid var(--border); }}
.report-header .eyebrow {{ font-size: 11px; font-weight: 600; letter-spacing: 1.5px; text-transform: uppercase; color: var(--text-tertiary); margin-bottom: 8px; }}
.report-header h1 {{ font-family: var(--font-serif); font-size: 36px; font-weight: 400; line-height: 1.2; margin-bottom: 8px; letter-spacing: -0.5px; }}
.report-header .meta {{ font-size: 14px; color: var(--text-secondary); display: flex; gap: 24px; align-items: center; flex-wrap: wrap; }}
.report-header .meta span {{ display: flex; align-items: center; gap: 6px; }}
.dot {{ width: 4px; height: 4px; border-radius: 50%; background: var(--text-tertiary); display: inline-block; }}
.dashboard {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin-bottom: 48px; }}
.threat-card {{ background: var(--accent); color: #FAFAF8; border-radius: 16px; overflow: hidden; transition: transform 0.2s ease, box-shadow 0.2s ease; }}
.threat-card:hover {{ transform: translateY(-2px); box-shadow: 0 8px 32px rgba(0,0,0,0.15); }}
.threat-card-header {{ padding: 20px 24px 16px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.08); }}
.threat-card-header .product-name {{ font-size: 16px; font-weight: 700; letter-spacing: -0.2px; }}
.threat-card-header .product-sub {{ font-size: 12px; font-weight: 400; opacity: 0.5; margin-left: 8px; }}
.threat-level-badge {{ font-family: var(--font-mono); font-size: 12px; font-weight: 600; letter-spacing: 1px; text-transform: uppercase; padding: 4px 12px; border-radius: 4px; }}
.threat-level-badge.high {{ background: rgba(220,38,38,0.2); color: #F87171; }}
.threat-level-badge.medium {{ background: rgba(217,119,6,0.2); color: #FBBF24; }}
.threat-level-badge.low {{ background: rgba(22,163,74,0.2); color: #4ADE80; }}
.threat-card-body {{ padding: 16px 24px 20px; }}
.confidence-line {{ display: flex; align-items: center; gap: 8px; margin-bottom: 12px; }}
.confidence-label {{ font-size: 11px; font-family: var(--font-mono); font-weight: 500; letter-spacing: 0.5px; text-transform: uppercase; color: rgba(250,250,248,0.35); }}
.confidence-dots {{ display: flex; gap: 4px; }}
.confidence-dot {{ width: 6px; height: 6px; border-radius: 50%; background: rgba(255,255,255,0.15); }}
.confidence-dot.filled {{ background: rgba(250,250,248,0.6); }}
.must-know {{ background: var(--surface); border-radius: 16px; padding: 28px 32px; margin-bottom: 48px; border: 1px solid var(--border); }}
.must-know h2 {{ font-family: var(--font-serif); font-size: 20px; font-weight: 400; margin-bottom: 16px; color: var(--text); }}
.must-know-list {{ list-style: none; }}
.must-know-list li {{ padding: 14px 0; border-bottom: 1px solid var(--border-light); display: flex; gap: 16px; align-items: flex-start; font-size: 14px; line-height: 1.55; color: var(--text); }}
.must-know-list li:last-child {{ border-bottom: none; padding-bottom: 0; }}
.must-know-list .num {{ font-family: var(--font-mono); font-size: 12px; font-weight: 500; color: var(--text-tertiary); min-width: 20px; padding-top: 2px; }}
.must-know-list .company-name {{ font-weight: 600; }}
.tabs {{ display: flex; gap: 4px; margin-bottom: 32px; background: var(--surface-alt); padding: 4px; border-radius: 12px; border: 1px solid var(--border); }}
.tab {{ flex: 1; padding: 10px 16px; border-radius: 8px; font-size: 13px; font-weight: 500; text-align: center; cursor: pointer; transition: all 0.2s ease; color: var(--text-secondary); border: none; background: transparent; font-family: var(--font); }}
.tab:hover {{ color: var(--text); background: rgba(0,0,0,0.03); }}
.tab.active {{ background: var(--surface); color: var(--text); box-shadow: 0 1px 3px rgba(0,0,0,0.08); }}
.tab-content {{ display: none; }}
.tab-content.active {{ display: block; }}
.section {{ margin-bottom: 36px; }}
.section h3 {{ font-size: 16px; font-weight: 600; margin-bottom: 4px; }}
.section .section-desc {{ font-size: 13px; color: var(--text-tertiary); margin-bottom: 16px; }}
.signal-card {{ background: var(--surface); border: 1px solid var(--border); border-radius: 12px; padding: 20px; margin-bottom: 12px; transition: border-color 0.2s; }}
.signal-card:hover {{ border-color: var(--text-tertiary); }}
.signal-card h4 {{ font-size: 14px; font-weight: 600; line-height: 1.4; margin-bottom: 8px; }}
.signal-card h4 .company-name {{ font-weight: 700; }}
.signal-card p {{ font-size: 13px; color: var(--text-secondary); line-height: 1.6; margin-bottom: 8px; }}
.signal-card .source {{ font-size: 12px; color: var(--text-tertiary); font-family: var(--font-mono); }}
.signal-card .source a {{ color: var(--blue-text); text-decoration: none; }}
.report-footer {{ margin-top: 48px; padding-top: 24px; border-top: 1px solid var(--border); }}
.report-footer p {{ font-size: 12px; color: var(--text-tertiary); line-height: 1.6; }}
.report-footer .sources-toggle {{ font-size: 13px; color: var(--text-secondary); cursor: pointer; display: inline-flex; align-items: center; gap: 6px; margin-top: 12px; border: none; background: none; font-family: var(--font); text-decoration: underline; text-underline-offset: 2px; }}
.sources-list {{ display: none; margin-top: 12px; font-size: 12px; color: var(--text-tertiary); font-family: var(--font-mono); line-height: 2; }}
.sources-list.show {{ display: block; }}
@keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(8px); }} to {{ opacity: 1; transform: translateY(0); }} }}
.dashboard .threat-card {{ animation: fadeIn 0.5s ease both; }}
.dashboard .threat-card:nth-child(2) {{ animation-delay: 0.1s; }}
.dashboard .threat-card:nth-child(3) {{ animation-delay: 0.2s; }}
.must-know {{ animation: fadeIn 0.5s ease 0.3s both; }}
@media (max-width: 768px) {{
  .container {{ padding: 24px 16px; }}
  .dashboard {{ grid-template-columns: 1fr; }}
  .report-header h1 {{ font-size: 28px; }}
  .tabs {{ flex-direction: column; }}
}}
</style>
</head>
<body>
<div class="container">

  <header class="report-header">
    <div class="eyebrow">OpenAI Competitive Intelligence</div>
    <h1>Weekly Intelligence Report</h1>
    <div class="meta">
      <span>Week of {escape(report["week_of"])}</span>
      <span class="dot"></span>
      <span>Generated {escape(report["generated"])}</span>
      <span class="dot"></span>
      <span>Agent v1.1</span>
    </div>
  </header>

  <div class="dashboard">
{"".join(threat_cards)}
  </div>

  <div class="must-know">
    <h2>Must know this week</h2>
    <ul class="must-know-list">
{"".join(must_know_items)}
    </ul>
  </div>

  <div class="tabs">
    <button class="tab active" onclick="showTab('chatgpt')">ChatGPT Intelligence</button>
    <button class="tab" onclick="showTab('codex')">Codex Intelligence</button>
    <button class="tab" onclick="showTab('api')">API & Models</button>
    <button class="tab" onclick="showTab('horizon')">Horizon Watch</button>
  </div>

  <div id="chatgpt" class="tab-content active">
{chatgpt_content}
  </div>

  <div id="codex" class="tab-content">
{codex_content}
  </div>

  <div id="api" class="tab-content">
{api_content}
  </div>

  <div id="horizon" class="tab-content">
{horizon_content}
  </div>

  <footer class="report-footer">
    <p>This report was generated by the OpenAI Competitive Intelligence Agent v1.1. All signals are sourced from publicly available information. Confidence scores reflect source corroboration, not strategic certainty. For internal use only.</p>
    <button class="sources-toggle" onclick="toggleSources()">View all sources consulted ↓</button>
    <div class="sources-list" id="sources">
      {sources_html}
    </div>
  </footer>

</div>
<script>
function showTab(tabId) {{
  document.querySelectorAll('.tab-content').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
  document.getElementById(tabId).classList.add('active');
  event.target.classList.add('active');
}}
function toggleSources() {{
  document.getElementById('sources').classList.toggle('show');
}}
</script>
</body>
</html>"""


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/generate_report.py <markdown_report_path> [-o output.html]")
        print("Example: python scripts/generate_report.py prior_reports/week_of_2026-03-23.md")
        sys.exit(1)

    md_path = Path(sys.argv[1])
    if not md_path.exists():
        print(f"Error: {md_path} not found")
        sys.exit(1)

    # Determine output path
    output_path = None
    if "-o" in sys.argv:
        idx = sys.argv.index("-o")
        if idx + 1 < len(sys.argv):
            output_path = Path(sys.argv[idx + 1])

    if output_path is None:
        output_path = md_path.with_suffix(".html")

    print(f"Reading:  {md_path}")
    content = md_path.read_text()

    print("Parsing report structure...")
    report = parse_report(content)

    print(f"  Threat levels: {len(report['threat_levels'])}")
    print(f"  Must-know items: {len(report['must_know'])}")
    print(f"  ChatGPT signals: {len(report['chatgpt_signals'])}")
    print(f"  Codex signals: {len(report['codex_signals'])}")
    print(f"  API signals: {len(report['api_signals'])}")
    print(f"  Horizon signals: {len(report['horizon_signals'])}")
    print(f"  Sources: {len(report['sources'])}")

    print(f"\nGenerating HTML...")
    html_content = generate_html(report)

    output_path.write_text(html_content)
    print(f"Output:   {output_path}")
    print(f"Done! Open {output_path} in a browser to view.")


if __name__ == "__main__":
    main()
