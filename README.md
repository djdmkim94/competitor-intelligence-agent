# Competitor Intelligence Agent

**Free, open-source AI agent that delivers daily competitive intelligence reports — styled, sourced, and ready for your exec team.**

Set up in 2 minutes. Uses your own Claude account. We never see your data.

---

## What It Does

Every morning (or on your schedule), this agent:

1. Scans the web for competitive signals — blog posts, product launches, executive tweets, developer sentiment, hiring patterns, open-source activity
2. Analyzes findings through your company's lens — which product line is affected, how urgent, how confident
3. Generates a structured report with threat levels, must-knows, and sourced findings
4. Delivers it as a styled HTML dashboard and markdown file

## Who It's For

- **Strategy & ops teams** tracking competitive landscape
- **Product managers** monitoring feature launches and benchmarks
- **Marketing leads** watching competitor messaging and positioning
- **Founders** who need a 5-minute daily brief on what competitors are doing

## Quick Start

### Option A: Use the Setup Wizard (non-technical)

1. Go to [the setup wizard](https://competitor-intel-agent.up.railway.app) and answer 5 questions
2. Download your generated `config.yaml`
3. Fork this repo and replace `config.yaml` with yours
4. Set up a [Claude Code scheduled trigger](https://claude.ai/code/scheduled) pointing to your fork

### Option B: Edit config directly

1. Fork this repo
2. Edit `config.yaml` — set your company, competitors, channels, and schedule
3. Set up a [Claude Code scheduled trigger](https://claude.ai/code/scheduled) pointing to your fork

### Option C: Run manually

```bash
# Clone and run with Claude Code
git clone https://github.com/djdmkim94/competitor-intelligence-agent.git
cd competitor-intelligence-agent
claude
# Then paste: "Read config.yaml and prompts/agent_system_prompt.md,
#   then run a competitive intelligence scan and generate the report."
```

## How It Works

```
config.yaml          →  Defines your company, competitors, channels
prompts/             →  System prompt that drives the agent
knowledge_base/      →  Baseline context (competitor profiles, benchmarks)
prior_reports/       →  Historical reports for trend detection
report_output/       →  Styled HTML dashboard reports
setup-wizard/        →  Browser-based config generator (setup-wizard branch)
```

## Report Structure

Each report includes:

| Section | Audience | What's In It |
|---|---|---|
| **C-Suite Dashboard** | CEO, CPO, CSO | Threat levels (HIGH/MED/LOW), confidence scores, top 3 must-knows |
| **Product Sections** | PMs, PMMs, BD | Findings organized by your product lines |
| **Hiring Signals** | Strategy | Job board patterns that reveal competitor intent |
| **Horizon Watch** | Everyone | Emerging challengers and future tech to monitor |
| **Sources** | Everyone | Every finding linked to its source URL |

## Customization

Everything is controlled by `config.yaml`:

- **Your company** — name, description, product lines
- **Competitors** — Tier 1 (deep weekly analysis), Tier 2 (weekly scan), Tier 3 (monthly horizon)
- **Search channels** — Reddit, Hacker News, Twitter/X, GitHub, job boards
- **Report settings** — schedule, format, threat level definitions

## Example Output

See real generated reports in `report_output/`:
- `week_of_2026-03-23.html` — styled HTML dashboard
- `week_of_2026-03-28.html` — styled HTML dashboard

## Cost

| Component | Cost |
|---|---|
| This repo | Free |
| Setup wizard | Free |
| Claude account | Your own account (Pro $20/mo or API usage) |
| Hosting (optional) | Railway free tier or Vercel free tier |

**The AI usage runs on your own Claude account.** We never see your API key or your reports.

## Tech Stack

- **Agent runtime**: Claude Code with web search
- **Config**: YAML (human-readable, easy to edit)
- **Reports**: Styled HTML + Markdown
- **Setup wizard**: Static HTML/CSS/JS (no backend)
- **Scheduling**: Claude Code scheduled triggers

## Contributing

PRs welcome. Main areas:
- Adding more competitor suggestion mappings to the setup wizard
- Improving the system prompt for better signal detection
- Adding new report sections or visualizations

## License

MIT

---

Built by [David Kim](https://github.com/djdmkim94) with Claude Code.
