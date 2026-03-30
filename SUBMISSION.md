# Competitor Intelligence Agent — OpenAI

## 1. Company and Strategic Context

OpenAI operates across three product lines — consumer (ChatGPT), enterprise coding (Codex), and developer platform (API/Models) — with revenue from freemium subscriptions, enterprise licensing, and per-token API pricing, competing against Anthropic, Google DeepMind, xAI, Cursor, Perplexity, and a rapidly growing Chinese open-source ecosystem (DeepSeek, Qwen, Zhipu AI, Moonshot/Kimi, MiniMax) that now accounts for 61% of global API token consumption on OpenRouter. This agent serves **OpenAI's C-suite, Product Managers, Product Marketing Managers, and Business Development leads**, delivering a weekly competitive intelligence report organized by product line so that each stakeholder receives only the signals relevant to their domain — ChatGPT signals go to PMMs, Codex signals go to PMs, and API/Models signals go to BD.

---

## 2. Agent Prompt

> The full, unabridged agent prompt is in `prompts/agent_system_prompt.md`. Below is the complete content.

```
You are a Competitive Intelligence Analyst embedded within OpenAI's Strategy & Operations team. Your job is to monitor, analyze, and synthesize competitive signals from publicly available sources into a structured weekly intelligence report.

## Your Audience

Your report serves multiple stakeholders at OpenAI. You organize intelligence by product line, with each section tailored to its primary consumer:

1. **C-Suite Dashboard** — For the CEO, CPO, CMO, and Chief Strategy Officer. This is the first thing they see. It must contain:
   - A threat-level indicator (HIGH / MEDIUM / LOW) for each product line
   - Confidence score for each threat rating (3-dot scale based on source corroboration)
   - A one-line "So What?" implication for each product line
   - A "Must Know This Week" section with the 3 most strategically significant signals across all product lines

2. **ChatGPT Section (PMM Lens)** — Consumer-facing product. Focus on:
   - Competitor messaging and positioning changes (how are they framing their consumer products?)
   - Customer sentiment and UX reactions on Twitter/X and Reddit
   - Marketing campaigns, brand moves, and GTM shifts by competitors
   - Gaps in competitor messaging that OpenAI could exploit
   - Competitor hiring patterns in marketing/growth roles (job board signals)

3. **Codex Section (PM Lens)** — Enterprise/prosumer product. Focus on:
   - New feature launches by competitors (especially Claude Code, Gemini Code Assist, Cursor, GitHub Copilot)
   - Benchmark comparisons and performance claims
   - Enterprise adoption signals (case studies, partnership announcements)
   - Developer sentiment and tool adoption trends on GitHub, Hacker News, Reddit
   - Competitor hiring patterns in engineering/product roles

4. **API & Models Section (BD/Partnerships Lens)** — Developer platform and ecosystem. Focus on:
   - New model releases, capabilities, and pricing changes
   - Partnership announcements (e.g., cloud provider integrations, hardware partnerships)
   - Open-source ecosystem shifts (new LLaMA releases, Hugging Face trends, DeepSeek activity)
   - Developer adoption and migration signals
   - Infrastructure and compute partnerships (AMD, NVIDIA, custom silicon)

## Competitors to Monitor

Competitors are organized by product line. Each report section should focus on its relevant competitor set.

### ChatGPT Competitors (Consumer AI Chat)
- **Anthropic** (Claude) — Primary rival, shifting from assistant → productivity platform
- **Google** (Gemini) — Strongest distribution advantage via Google ecosystem
- **xAI** (Grok) — Consumer niche via X/Twitter, 2M context, aggressive scaling
- **Perplexity** — Redefining search-as-chat, overlaps with ChatGPT use cases

### Codex Competitors (AI Coding Tools)
- **Cursor / Anysphere** — Fastest-growing AI coding tool, AI-native IDE
- **Anthropic** (Claude Code) — Best SWE-Bench scores, agentic CLI approach
- **Google** (Gemini Code Assist, Jules) — Free tier for teams <25, aggressive pricing
- **GitHub Copilot** — Incumbent with largest installed base
- **Cognition** (Devin + Windsurf) — Full-spectrum AI coding: Windsurf IDE (copilot) + Devin (autonomous agent). Most comprehensive coding competitor after acquiring Windsurf/Codeium.

### API & Models Competitors (Developer Platform)

**Closed-source APIs:**
- **Anthropic** (Claude API) — Tied #1 on Arena, dominant in agentic/coding workloads
- **Google** (Gemini API) — Best price-performance ratio, 1M context
- **xAI** (Grok API) — Leading agentic index, 2M context
- **Meta** (LLaMA API) — Open-weight + API hybrid model
- **Mistral** (Mistral API) — EU sovereignty, Apache 2.0, GDPR-compliance moat

**Open-source / open-weight models (eroding API revenue):**
- **DeepSeek** (V3.2, R1) — Beats GPT-5 on some reasoning benchmarks, massive adoption
- **Alibaba / Qwen** (Qwen 3.5) — 48 variants, competes with GPT-5.2 on benchmarks
- **Zhipu AI** (GLM-5) — Best open-source coding (95.8% SWE-bench), MIT license, Huawei chips
- **Moonshot AI** (Kimi K2.5) — #2 by token usage on OpenRouter, MIT license
- **MiniMax** (M2.5) — #1 by raw token usage on OpenRouter, strong agent workloads
- **ByteDance** (Seed 2.0) — #6 Arena overall, aggressive pricing
- **NVIDIA** (Nemotron) — Free tier models driving experimentation

**Key market signal:** Chinese models now account for 61% of total token consumption on OpenRouter. Programming is 50%+ of all API tokens.

### Horizon Watch (Monthly scan)
- World models and video understanding (Runway, Pika, MiniMax Hailuo, ByteDance, Google Veo)
- Robotics-AI convergence (Figure AI, 1X, Boston Dynamics, Tesla Optimus)
- Agentic framework evolution (LangChain, CrewAI, AutoGen adoption)
- Open-source ecosystem shifts and new paradigms

## Data Sources

You have access to the following tools and should use them in this priority order:

1. **Web Search** — For competitor news, announcements, blog posts, press releases, and funding news
2. **Exa Search** — For semantic search across competitor narratives, trend detection, and finding related content
3. **Twitter/X Monitoring** — Search for posts from key executives, product leads, and AI researchers. **Important**: Only surface tweets about AI products, launches, partnerships, or strategy. Ignore personal tweets, jokes, memes, and off-topic content. Use engagement metrics (likes, reposts) as a relevance proxy — low-engagement posts from execs are likely personal. When in doubt, exclude rather than include:
   - Anthropic: @DarioAmodei, @DanielaAmodei, @mikeyk (CPO Mike Krieger), @bcherny (Boris Cherny, Claude Code lead), @AmandaAskell (alignment), @ch402 (Chris Olah, interpretability), @janleike (alignment science)
   - Google DeepMind: @demishassabis, @sundarpichai, @JeffDean, @simpsoka (Kathy Korevec, Jules/Google Labs lead)
   - xAI: @elonmusk
   - Meta AI: @ylecun (Yann LeCun), @Ahmad_Al_Dahle (VP GenAI)
   - Cursor: @mntruell (Michael Truell, CEO), @amanrsanger (Aman Sanger, COO), @sualehasif996 (Sualeh Asif, CPO)
   - Cognition: @ScottWu46 (Scott Wu, CEO), @walden_yan (Walden Yan, CPO)
   - Perplexity: @AravSrinivas (Aravind Srinivas, CEO), @denisyarats (Denis Yarats, CTO)
   - Mistral: @arthurmensch (Arthur Mensch, CEO), @GuillaumeLample (Chief Scientist), @sophiamyang (DevRel lead)
   - Chinese AI (company accounts): @deepseek_ai, @Kimi_Moonshot, @Zai_org (Zhipu/GLM), @Alibaba_Qwen, @MiniMax__AI, @Hailuo_AI, @doubaoAi
   - GitHub/Copilot: @kdaigle (Kyle Daigle, COO)
4. **Job Board Search** — Monitor career pages of competitors for:
   - New role types that signal strategic shifts (e.g., "world model researcher," "enterprise sales - healthcare")
   - Volume changes in specific departments (hiring surges = investment signals)
   - Seniority patterns (leadership hires = new initiatives)
5. **GitHub Activity** — Monitor open-source repos, star velocity, new releases
6. **Reddit/Hacker News** — Developer sentiment, product reactions, adoption discussions
7. **Leaderboard & Marketplace Monitoring** — Track competitive positioning on key platforms:
   - **LMSYS Chatbot Arena** (lmarena.ai) — Human-preference Elo rankings; watch for rank changes and new entrants
   - **OpenRouter Rankings** (openrouter.ai/rankings) — Token usage by model; adoption shifts and pricing changes
   - **HuggingFace Open LLM Leaderboard** — Benchmark scores for open-weight models that could erode API revenue
   - **SWE-Bench Verified** (swebench.com) — Real-world coding benchmark; critical for Codex competitive positioning

## Analysis Framework

For each signal you find, evaluate:

1. **Relevance**: Does this affect one of OpenAI's product lines? Which one(s)?
2. **Urgency**: Is this a threat that requires immediate response, or a trend to monitor?
3. **Confidence**: How reliable is this signal? (Single source = LOW, multiple corroborating sources = HIGH)
4. **Strategic Implication**: What does this mean for OpenAI? Frame as an implication, not a recommendation. Let decision-makers decide what to do.

## Threat-Level Rating Criteria

- **HIGH**: Competitor has launched or announced something that directly threatens OpenAI's market position in a product line. Multiple corroborating sources. Requires leadership attention this week.
- **MEDIUM**: Notable competitive signal that indicates a strategic shift or emerging threat. Should be on leadership's radar. May require response within 2-4 weeks.
- **LOW**: No significant competitive threats detected this week. Business as usual, but include noteworthy signals for awareness.

## Output Format

Structure every finding as: **Company Name** — Description of the signal

Generate a structured report with these sections:
1. **Report Header**: Week of [date range], generated on [date]
2. **C-Suite Dashboard**: Threat indicators, confidence scores, must-knows
3. **ChatGPT Intelligence** (PMM): Messaging, sentiment, marketing signals
4. **Codex Intelligence** (PM): Features, benchmarks, enterprise signals
5. **API & Models Intelligence** (BD): Models, partnerships, ecosystem
6. **Hiring & Resource Signals**: Cross-cutting job board analysis
7. **Horizon Watch**: Rising challengers + future tech
8. **Sources**: Full list of sources consulted with URLs

## Important Guidelines

- Be specific. Cite sources for every claim. Never fabricate signals.
- Distinguish between confirmed facts and speculation/rumors.
- When you find conflicting information across sources, flag the discrepancy.
- If you cannot find meaningful signals for a section in a given week, say so explicitly. Do not pad with generic observations.
- Prioritize signal over noise. An executive reading this report should be able to make decisions within 5 minutes.
- Frame implications neutrally. Your job is to surface what's happening and what it might mean — not to tell leadership what to do.
- Always start each finding with the company name in bold, followed by an em dash, then the signal.

## Knowledge Base

Before generating a report, read the following files for context:
- `knowledge_base/openai_context.md` — OpenAI's products and strategic priorities
- `knowledge_base/competitor_profiles.md` — Baseline competitor profiles organized by product line (detect deltas, not restate)
- `knowledge_base/industry_benchmarks.md` — Quantitative benchmarks, Arena rankings, and pricing data
- `prior_reports/exa_scan_YYYY-MM-DD.md` — Pre-fetched Exa semantic search signals (primary input)
- `prior_reports/` — Previous weekly reports for trend detection

**Critical**: The knowledge base provides baseline context and competitor structure, but it may be stale. When live search results (web search, Exa, leaderboards) conflict with knowledge base data — such as a different model version, valuation, or product status — **always trust the live data** and note the discrepancy. The knowledge base is a starting point for what to look for, not ground truth for what exists.
```

---

## 3. Technologies Used

| Technology | Category | Justification |
|---|---|---|
| **Claude (Anthropic API)** | LLM Platform | Long context window (200K–1M tokens) handles synthesis of large volumes of competitor text from multiple sources in a single pass. Strong structured output capabilities for generating the 8-section report schema consistently. Selected over GPT-4o because of superior instruction-following on complex multi-section outputs. |
| **Claude Code** | Agent Runtime / Orchestration | Natural-language-driven agent runtime with built-in web search, file read/write, and tool use. Runs locally with system prompt injection. Selected because it allows non-engineers on the team to iterate on the agent by editing markdown files rather than writing code. |
| **Exa API** (`exa-py` SDK, exa.ai) | Semantic Search & Monitoring | Neural search API that finds pages by *concept similarity*, not just keyword match — critical for detecting narrative and positioning shifts (e.g., "how is Anthropic positioning Claude for enterprise"). Pre-scan script (`exa_scan.py`) runs 19 queries across 4 product-line sections before each agent run, saving ~50-100 deduplicated signals to markdown. Selected over Google Custom Search because semantic queries outperform keyword queries for competitive positioning analysis. |
| **Web Search** (Claude Code built-in) | Real-time Search | Claude Code's built-in web search for time-sensitive breaking news, press releases, and announcements. Complements Exa: web search for recency, Exa for depth. |
| **Playwright** (`playwright` Python SDK) | PDF Generation | Renders the HTML report in a headless Chromium browser and exports to A4 PDF with full CSS fidelity (dark threat cards, fonts, grid layout). Selected over WeasyPrint (broken gobject dependency on macOS) and wkhtmltopdf (not installed). |
| **Resend** (`resend` Python SDK, resend.com) | Email Delivery | Sends the HTML report as email body + PDF attachment via API. Simple integration (5 lines of code), no SMTP configuration needed. Selected over SendGrid/SES for simplicity and free tier (100 emails/day). |
| **Markdown Files** (local) | Data Storage / Knowledge Base | Lightweight, version-controllable, human-readable storage for company context, competitor profiles, benchmark data, prompt logs, and historical reports. Agent reads these files at the start of every run. Selected over a database because the knowledge base is small (<50KB total) and benefits from direct human editing. |
| **HTML/CSS/JS** | Output Rendering | Final report delivered as a polished HTML dashboard with dark threat cards, confidence dots, tabbed product-line sections, and expandable source lists. `generate_report.py` converts agent markdown output → styled HTML programmatically. Designed for executive consumption via email or browser. |
| **`run_agent.sh`** | Pipeline Orchestration | Shell script that orchestrates the full agent pipeline: (1) Exa pre-scan, (2) Claude Code agent with system prompt, (3) HTML generation via `generate_report.py`, (4) PDF + email via `send_report.py`. Single-command execution for weekly report cycle. |
| **`run_eval.py`** | Evaluation Framework | Python script that runs 10 test scenarios against real agent output using LLM-as-judge (Claude). Scores on 5 dimensions (signal detection, classification, threat level, citation, actionability). Outputs structured eval results to `eval/eval_results.md`. |
| **GitHub** | Version Control & Collaboration | All prompt files, scripts, knowledge base documents, and reports stored in a shared repo. Enables team collaboration, prompt iteration tracking, and submission packaging. |

---

## 4. Inputs

### Primary Inputs (Collected Weekly)

| Input | Type | Source | Structured? | Preprocessing |
|---|---|---|---|---|
| Competitor blog posts & announcements | Unstructured text | Exa search + web search targeting anthropic.com/blog, deepmind.google/blog, x.ai/blog, ai.meta.com/blog | No | Extracted as clean markdown via search tools, then passed to Claude for summarization and signal extraction |
| Twitter/X posts from key people | Unstructured text | Web search filtered to twitter.com/x.com for 30+ monitored accounts across all competitors (founders, CPOs, product leads, AI researchers, company accounts for Chinese AI firms) | No | Filtered for AI/product-related content. Engagement metrics (likes, reposts) noted as sentiment proxy |
| Job postings from competitor career pages | Semi-structured | Web search targeting careers.anthropic.com, careers.google.com, xai job boards, meta careers | Semi | Role titles, departments, and seniority levels extracted. Categorized by function (engineering, marketing, sales, research) and compared to prior week |
| GitHub repository activity | Structured | GitHub search for org repos (anthropic, google-deepmind, meta-llama, xai-org), sorted by recently updated | Yes | Star counts, commit frequency, new repos flagged. Compared to baseline from prior week |
| Reddit & Hacker News threads | Unstructured text | Web search filtered to reddit.com/r/LocalLLaMA, r/ChatGPT, r/ClaudeAI, news.ycombinator.com | No | Filtered for competitor product mentions with >50 upvotes. Sentiment classified as positive/negative/neutral |
| News articles & press releases | Unstructured text | Exa search for competitor names + keywords (funding, partnership, launch, acquisition) | No | Deduplicated across sources. Classified by relevance to product lines |
| Leaderboard & marketplace rankings | Structured | LMSYS Chatbot Arena (lmarena.ai), OpenRouter Rankings (openrouter.ai/rankings), HuggingFace Open LLM Leaderboard, SWE-Bench Verified (swebench.com) | Yes | Elo rankings, token usage volumes, benchmark scores tracked week-over-week. Rank changes and new model entries flagged as signals. Critical for API & Models competitive positioning. |
| Exa pre-scan results | Semi-structured | `exa_scan.py` runs 24 semantic search queries across 5 sections (ChatGPT, Codex, API, Hiring, Horizon) via Exa API before each agent run | Yes | Results deduplicated by URL within each section, filtered by `start_published_date`, saved to `prior_reports/exa_scan_YYYY-MM-DD.md`. Agent reads this as primary input alongside web search. In our test run, this produced 95 unique signals including one that web search missed entirely (Cursor's Composer 2 built on Moonshot AI's Kimi K2.5). |

### Internal Knowledge Inputs (Persistent)

| Input | Type | Purpose |
|---|---|---|
| `openai_context.md` | Company profile | OpenAI's product lines, strategic priorities, current positioning — provides the lens through which competitive signals are evaluated |
| `competitor_profiles.md` | Competitor baselines | Competitor profiles organized by product line: ChatGPT (consumer), Codex (coding tools), API & Models (closed-source + open-source). Includes detailed profiles for 20+ competitors with positioning, strengths, threat levels. Enables the agent to detect *changes* rather than re-describing known info |
| `prior_reports/` | Historical reports | Previous weekly reports stored as markdown — enables trend detection and "this changed since last week" analysis |
| `prompt_log.md` | Prompt history | Log of all prompt iterations (v1.0 by David, v1.1 by Jack) with design decisions, rationale, and known issues for each version. Required for assignment deliverable. |
| `exa_scan_YYYY-MM-DD.md` | Pre-fetched Exa signals | 50-100 deduplicated semantic search results from Exa API, organized by product-line section (ChatGPT, Codex, API, Hiring, Horizon). Generated fresh by `exa_scan.py` before each agent run. |

---

## 5. Outputs

### Output Schema

The agent produces a weekly HTML intelligence report with the following structure:

```json
{
  "report_metadata": {
    "week_of": "2026-03-23 to 2026-03-29",
    "generated_on": "2026-03-28",
    "agent_version": "1.1"
  },
  "c_suite_dashboard": {
    "must_know_this_week": [
      {
        "signal": "string — one-line description",
        "product_line_affected": "chatgpt | codex | api | multiple",
        "source": "string — URL or source name"
      }
    ],
    "threat_levels": {
      "chatgpt": {
        "level": "HIGH | MEDIUM | LOW",
        "confidence": "HIGH | MEDIUM | LOW",
        "rationale": "string — one sentence",
        "implication": "string — one-line 'So What?'"
      },
      "codex": { "..." },
      "api_models": { "..." }
    }
  },
  "chatgpt_intelligence": {
    "messaging_shifts": [],
    "sentiment_signals": [],
    "marketing_moves": [],
    "hiring_signals": []
  },
  "codex_intelligence": {
    "feature_launches": [],
    "benchmark_updates": [],
    "enterprise_signals": [],
    "developer_sentiment": [],
    "hiring_signals": []
  },
  "api_models_intelligence": {
    "model_releases": [],
    "partnership_moves": [],
    "ecosystem_shifts": [],
    "pricing_changes": []
  },
  "horizon_watch": {
    "rising_challengers": [],
    "future_tech": []
  },
  "sources": []
}
```

### Reporting Cadence

- **Weekly comprehensive report**: Full HTML dashboard covering all product lines, generated every Monday morning. Delivered via email (HTML body + PDF attachment) using Resend API.
- **Daily alert**: Abbreviated signal-level report with RED/YELLOW classification. Lightweight format listing the top 3-5 signals requiring immediate attention. Template implemented in v1.1 (see `prior_reports/daily_2026-03-29.md`).

### Output Consumer

- **Primary**: C-suite (CEO, CPO, CMO, Chief Strategy Officer) — via the dashboard header
- **Secondary**: Product Managers (Codex section), Product Marketing Managers (ChatGPT section), Business Development (API/Models section)

### Confidence Scoring

Confidence scores are applied at the **threat-level rating** level (not individual findings) to balance informativeness with token efficiency:

- **HIGH**: Signal corroborated by 3+ independent sources or is a primary source (official blog post, press release)
- **MEDIUM**: Signal from 2 sources or a single credible source (major news outlet, verified executive tweet)
- **LOW**: Single source, unverified, or based on inference/rumor

### Sample Output

The following is a real excerpt from a report generated by the agent on March 29, 2026, using live web search and Exa semantic search data. The full report is in `prior_reports/week_of_2026-03-23.md` (17,420 bytes, 26 cited source URLs).

#### C-Suite Dashboard

| Product Line | Threat Level | Confidence | This Week's Key Signal | So What? |
|---|---|---|---|---|
| **ChatGPT** | HIGH | ●●● | Anthropic had 14+ product launches in March (Claude Apps, Cowork, computer use); Google launched ChatGPT-to-Gemini migration tool; Perplexity evolved into full AI platform with Personal Computer hardware | Three competitors made simultaneous moves against ChatGPT's core retention: Anthropic with always-on agents, Google with direct migration tooling, and Perplexity with a hardware-backed autonomous assistant. |
| **Codex** | HIGH | ●●● | Cursor raised $2.3B at $29.3B valuation, launched autonomous cloud agents (Automations), acquired Graphite; Google shipped Jules GA powered by Gemini 3 Pro; Claude Code leads SWE-Bench | Codex faces a three-front war: Cursor is now a $29B autonomous agents platform, Google's Jules is GA with aggressive pricing, and Claude Code leads benchmarks. |
| **API/Models** | HIGH | ●●● | DeepSeek V4 imminent (multimodal, 1T params, tops LMSYS coding leaderboard); Chinese models 61% of OpenRouter tokens; Zhipu GLM-5 at 95.8% SWE-bench under MIT license on Huawei chips | Open-source models trained on non-US hardware are reaching frontier performance at 1/50th the cost. The API pricing moat is eroding faster than any prior quarter. |

#### Must Know This Week (top 3)

1. **Anthropic** — Claude Mythos leak reveals next-gen model described as "step change in capabilities" with "unprecedented cybersecurity risks." Anthropic considering IPO as early as October 2026. 14+ product launches in March alone. ([Fortune](https://fortune.com/2026/03/26/anthropic-says-testing-mythos-powerful-new-ai-model-after-data-leak-reveals-its-existence-step-change-in-capabilities/), [Bloomberg](https://www.bloomberg.com/news/articles/2026-03-27/claude-ai-maker-anthropic-said-to-weigh-ipo-as-soon-as-october))

2. **Cursor / Anysphere** — Raised $2.3B at $29.3B valuation. Launched Automations (autonomous cloud agents) on March 5. Acquired Graphite (code review). 60% of revenue now from enterprise (OpenAI, Uber, Spotify, Shopify, NVIDIA). ([TechFundingNews](https://techfundingnews.com/anysphere-soars-to-29-3b-valuation-with-2-3b-funding-redefining-the-future-of-coding/))

3. **Google** — Launched ChatGPT-to-Gemini chat history migration tool, directly targeting ChatGPT user retention. Jules coding agent exits beta with Gemini 3 Pro. Gemini Code Assist now free for individual developers. ([Bloomberg](https://www.bloomberg.com/news/articles/2026-03-26/google-gemini-adds-tool-to-make-it-easier-to-switch-from-chatgpt))

#### Sample Signal — Codex Section Excerpt

**Cursor** — Launched Automations on March 5: autonomous cloud agents that execute coding tasks without human-in-the-loop. This shifts Cursor from "smart editor" to "platform for autonomous cloud agents." Also acquired Graphite (code review tool) to address the debugging bottleneck in AI-generated code. Enterprise revenue now 60% of total. Clients: OpenAI, Uber, Spotify, Shopify, NVIDIA, MLB. (Source: [InfoWorld](https://www.infoworld.com/article/4110558/cursor-owner-anysphere-agrees-to-buy-graphite-code-review-tool.html), [Contrary Research](https://research.contrary.com/company/cursor))

---

## 6. Knowledge Sources Used

| Knowledge Source | Type | Purpose | Update Frequency |
|---|---|---|---|
| `openai_context.md` | Internal company context | Encodes OpenAI's product descriptions (ChatGPT, Codex, API), strategic priorities, target markets, and key differentiators. Provides the "lens" through which all competitive signals are evaluated. | Updated manually when OpenAI's strategy shifts |
| `competitor_profiles.md` | Persistent competitor profiles | Baseline profiles for 20+ competitors organized by product line (ChatGPT, Codex, API & Models): products, positioning, funding, leadership, threat levels. Enables the agent to detect *deltas* (what changed) rather than restating known information. | Updated weekly as part of report generation |
| `prior_reports/` directory | Historical intelligence | Archive of all prior weekly reports in markdown. Enables trend analysis ("Anthropic's hiring in enterprise sales has increased 3 weeks in a row") and prevents duplicate reporting. | Auto-appended after each report run |
| `industry_benchmarks.md` | Industry context | LMSYS Chatbot Arena Elo rankings, SWE-Bench Verified, GPQA, MMLU scores for 15+ models (both open-source and closed). API pricing tables for closed-source and open-weight models. Market context including Chinese model dominance (61% of OpenRouter tokens) and coding workload shifts. | Updated monthly or when major benchmarks are published |
| `exa_scan_YYYY-MM-DD.md` | Pre-fetched Exa signals | 50-100 deduplicated semantic search results from Exa API, organized by product-line section. Generated by `exa_scan.py` before each agent run. Provides the agent with deeper narrative/positioning signals that keyword-based web search misses. | Generated fresh before each agent run |
| Agent system prompt | Encoded strategic assumptions | The prompt itself encodes assumptions about: which competitors matter most (product-line-first framework), which signals are relevant to which product lines, and what constitutes a threat vs. noise. These are strategic choices, not neutral defaults. | Updated when the monitoring framework changes |

---

## 8. Tools the Agent Has Access To

### Tool 1: Web Search

- **What it does**: Performs real-time web searches and returns structured results with titles, snippets, and URLs
- **When it is used**: First-pass data gathering for every section — competitor news, press releases, blog posts, product announcements, job postings
- **How the agent decides to use it**: Default tool for broad keyword queries (e.g., "Anthropic announcement March 2026," "Google Gemini Code Assist launch"). Used when the agent needs current, time-bounded information.
- **Known failure modes**: Can return outdated or irrelevant results for ambiguous queries. Snippet-level results sometimes lack context, requiring follow-up with Exa or direct URL fetching. Rate limits may throttle during parallel agent runs.

### Tool 2: Exa Search (API — connected)

- **What it does**: Neural/semantic search that finds pages similar to a concept or query, returning clean content and metadata. Better than keyword search for detecting narrative and positioning shifts. Connected via `exa-py` SDK with API key.
- **When it is used**: Pre-scan script (`scripts/exa_scan.py`) runs 19 queries across 4 product-line sections before each agent run, saving ~50-100 unique signals to `prior_reports/exa_scan_YYYY-MM-DD.md`. The agent reads this file as primary input alongside web search.
- **How the agent decides to use it**: Exa results are pre-fetched and available as a file. The agent cross-references Exa signals with web search results for corroboration. Exa is preferred for narrative/positioning queries; web search is preferred for time-sensitive breaking news.
- **Known failure modes**: May surface older content if the semantic match is strong but the publication date is stale (mitigated by `start_published_date` filter). Can over-index on SEO-optimized content. Rate limits on free tier (~1000 searches/month).

### Tool 3: URL Fetch / Web Scrape

- **What it does**: Retrieves the full content of a specific URL as clean markdown
- **When it is used**: When the agent has identified a specific competitor page (blog post, careers page, product documentation) and needs the complete content rather than a search snippet
- **How the agent decides to use it**: Triggered when a search result looks highly relevant but the snippet is insufficient. Also used for recurring monitoring targets (e.g., competitor career pages, changelog pages).
- **Known failure modes**: Some sites block automated access or require JavaScript rendering. Career pages on Greenhouse/Lever may not return full listings via simple fetch. LinkedIn is largely inaccessible to scraping.

### Tool 4: File Read / Knowledge Base Search

- **What it does**: Reads local markdown files from the knowledge base (company context, competitor profiles, prior reports)
- **When it is used**: At the start of every report generation cycle to load context, and during analysis to compare current signals against historical baselines
- **How the agent decides to use it**: Always runs at report initialization. During analysis, the agent references prior reports to identify trends and avoid duplicate findings.
- **Known failure modes**: Knowledge base may be stale if not updated. If the prior report was generated with errors, those errors can propagate into trend analysis.

### Tool 5: Leaderboard & Marketplace Monitoring

- **What it does**: Fetches and compares current rankings from LMSYS Chatbot Arena (Elo rankings), OpenRouter (token usage/adoption), HuggingFace Open LLM Leaderboard (benchmark scores), and SWE-Bench Verified (coding benchmarks)
- **When it is used**: Every weekly report cycle, specifically for the API & Models section and Codex section (SWE-Bench). Provides quantitative competitive positioning data that complements qualitative signals from news/Twitter.
- **How the agent decides to use it**: Always checked as part of the API & Models analysis. Rank changes, new model entries, and significant token usage shifts are flagged as signals. Week-over-week comparisons against `industry_benchmarks.md` baselines.
- **Known failure modes**: Rankings can fluctuate with small Elo changes that aren't strategically meaningful. OpenRouter token usage reflects developer experimentation, not necessarily enterprise adoption. Self-reported benchmarks may not match independent evaluations.

### Tool 6: HTML Report Generator (`generate_report.py`)

- **What it does**: Parses the agent's markdown report output and generates a styled HTML dashboard with dark threat cards, confidence dots, tabbed product-line sections, and expandable source lists.
- **When it is used**: Automatically after the agent saves its markdown report. Converts structured markdown → polished HTML for executive consumption.
- **How the agent decides to use it**: Not a decision — it's an automatic pipeline step triggered by `run_agent.sh` after the agent run completes.
- **Known failure modes**: Parser relies on the agent following the expected output format (bold company names, section headers, confidence dots). When the agent deviated (e.g., using `●●●` instead of text), the parser broke — we found and fixed 3 regex bugs during testing (see Failure 5).

### Tool 7: Email Delivery (`send_report.py`)

- **What it does**: Generates a PDF from the HTML report using Playwright (headless Chromium), then sends the HTML as the email body with the PDF as an attachment via Resend API.
- **When it is used**: Final pipeline step. Automatically sends the completed report to stakeholders after HTML generation.
- **How the agent decides to use it**: Not a decision — automatic pipeline step. Default recipient is configurable. Supports `--dry-run` for testing.
- **Known failure modes**: Resend's test sender (`onboarding@resend.dev`) can only send to the account owner's email. Sending to arbitrary recipients requires a verified domain. PDF generation requires Playwright's Chromium binary to be installed.

### Tool Selection Logic

The agent follows a sequential pipeline:
1. **Pre-scan** (Tool 2) → `exa_scan.py` runs 19 Exa semantic searches across all competitor sections, saves ~50-100 signals to markdown
2. **Load context** (Tool 4) → Read company context, competitor profiles, benchmark baselines, AND pre-fetched Exa scan
3. **Broad search** (Tool 1) → Web search for each competitor by product line (complements Exa with breaking news)
4. **Leaderboard check** (Tool 5) → Fetch current Arena, OpenRouter, HuggingFace, and SWE-Bench rankings; compare to baselines
5. **Targeted fetch** (Tool 3) → Pull full content from high-signal URLs
6. **Synthesize** → Cross-reference Exa signals + web search + leaderboards against knowledge base, generate report
7. **Deliver** → Generate HTML via `generate_report.py`, PDF + email via `send_report.py`

When multiple tools could serve the same query, the agent prefers Exa for narrative/positioning signals, web search for time-sensitive breaking news, and leaderboards for quantitative positioning.

---

## 9. What the Agent Does Well

### Product-Line Routing Eliminates Irrelevant Noise
In the March 23–29 test run, the agent surfaced 26 unique signals from web search and 95 from Exa. Without product-line routing, a Codex PM would have to read all 121 signals to find the ~20 relevant to coding tools. With routing, the Codex section contained exactly 6 signals — all directly about Cursor, Claude Code, Gemini Code Assist, or Cognition. The ChatGPT PMM never sees API pricing changes; the BD lead never sees consumer sentiment threads. In a manual analyst workflow, this filtering step takes 2-3 hours per week.

### Exa Semantic Search Catches Signals Web Search Misses
In our test run, Exa's semantic search surfaced a signal that web search completely missed: Cursor's Composer 2 model is secretly built on Moonshot AI's Kimi K2.5 ([TechCrunch](https://techcrunch.com/2026/03/22/cursor-admits-its-new-coding-model-was-built-on-top-of-moonshot-ais-kimi/)). This is strategically significant — it means Cursor's product moat depends on a Chinese open-source model, which has supply chain and licensing implications. Keyword-based web search for "Cursor news" returned funding/valuation articles, not this deeper dependency signal. Exa found it because the query "Cursor AI coding tool" semantically matched an article about Cursor's model sourcing.

### Quantitative Leaderboard Data Removes Ambiguity
The agent checks LMSYS Chatbot Arena Elo rankings, OpenRouter token usage, and SWE-Bench Verified scores as structured data inputs. In the test run, this produced a concrete finding: "DeepSeek V4 tops LMSYS Coding Leaderboard alongside Claude 4.6 for Python, at 1/50th the cost of GPT-5.4." This is a harder signal than "developers seem to like DeepSeek" — it gives leadership a specific, quantified competitive position to respond to.

### Automated Delivery Reduces Time-to-Decision
The full pipeline — Exa pre-scan → agent synthesis → markdown → HTML → PDF → email — runs end-to-end without human intervention. In the test run, the agent generated a 17,420-byte weekly report with 26 cited URLs, converted it to a styled HTML dashboard, generated a 216KB PDF, and emailed both to the recipient in under 3 minutes. A human analyst producing an equivalent report would spend 6-8 hours per week gathering, filtering, synthesizing, and formatting.

### Confidence Scoring Prevents Over-Reaction
By applying confidence scores (HIGH/MEDIUM/LOW based on source corroboration) at the threat-level rating level, the agent distinguishes between "Google launched a ChatGPT migration tool" (HIGH — confirmed by Bloomberg and Google's own blog) and "DeepSeek V4 reportedly surpasses GPT-5" (MEDIUM — based on leaked benchmarks, no official release). This prevents leadership from reacting to rumors with the same urgency as confirmed launches.

---

## 10. Where the Agent Fails

### Failure 1: LinkedIn Data Inaccessibility
**What happened**: Our initial design included LinkedIn company posts and employee data as a primary signal source — this was a key discussion point in our team planning. When we attempted to implement this, we discovered that LinkedIn aggressively blocks scraping, and no reliable API exists for the signals we wanted (company post engagement, employee count changes, role distribution).

**Impact**: We lost a significant signal source for hiring patterns and executive announcements. LinkedIn is where many AI companies make partnership and leadership announcements first.

**Fix**: We pivoted to using job board career pages directly (careers.anthropic.com, etc.) and Twitter/X for executive signals. This covers ~70% of what LinkedIn would have provided, but we lose company-level engagement metrics and employee network analysis.

### Failure 2: Hallucinated Competitive Signals
**What happened**: In early testing, the agent occasionally generated plausible-sounding but fabricated competitive signals — for example, reporting a "partnership between Anthropic and AMD" that did not exist. The structured output format made these fabrications *more dangerous* because they appeared authoritative within the report schema.

**Impact**: A fabricated RED-level threat could cause leadership to make decisions based on false intelligence — the worst possible outcome for a competitive intelligence tool.

**Fix**: We added explicit instructions in the prompt to cite sources for every claim, distinguish between confirmed facts and speculation, and flag when a signal comes from a single unverified source. We also added the confidence scoring system to make source reliability transparent. The agent now explicitly states "No significant signals detected" rather than padding sections with weak findings.

### Failure 3: Twitter/X Signal Noise
**What happened**: When monitoring executive Twitter accounts, the agent initially surfaced personal tweets, retweets of unrelated content, and jokes alongside genuine product signals. A sarcastic tweet by Elon Musk about AI was classified as a strategic signal.

**Impact**: The ChatGPT section's sentiment analysis was polluted with irrelevant content, reducing trust in the report.

**Fix**: We refined the prompt to filter for AI/product-related content only and to evaluate engagement metrics (likes, reposts) as a relevance proxy. We also instructed the agent to ignore tweets that are clearly personal or humorous in nature. This reduced noise by ~60%, but some false positives persist.

### Failure 4: Knowledge Base Stale Within Hours of Being Written
**What happened**: We updated all three knowledge base files on the morning of March 29, 2026, incorporating research from HuggingFace and OpenRouter. When we ran the agent that same afternoon with live web search, we discovered 10 factual errors in the knowledge base we had just written:
- Our profiles listed DeepSeek V3.2 as the latest model — but V4 (multimodal, 1T params) had appeared on DeepSeek's website on March 9
- We listed Cursor at ~$10B valuation — but they had raised $2.3B at $29.3B valuation that same week
- We described Perplexity as "search-as-chat" — but they had launched Personal Computer (hardware), a full API platform, and enterprise products
- We had GPT-5.2 as OpenAI's latest — but GPT-5.4 had already launched
- We said Cognition's Devin and Windsurf were "integrated" — but the SF Standard reported they "remain largely separate"

**Impact**: The knowledge base was stale enough to produce incorrect threat levels. If the agent had used our morning-written profiles without cross-referencing live search, it would have under-classified Cursor ($10B → $29.3B is a different strategic conversation) and missed Perplexity's platform evolution entirely.

**Fix**: We corrected all 10 errors and added a design principle: the knowledge base provides *baseline context and competitor structure*, but the agent must always cross-reference against live search results before finalizing any threat level or signal. The knowledge base is a starting point, not ground truth.

### Failure 5: Report Parser Broke on Real Agent Output
**What happened**: We built `generate_report.py` to convert the agent's markdown report into a styled HTML dashboard. When we ran it on a real agent output for the first time, it extracted 0 threat levels, 0 must-know items, and 0 API section signals — even though all of those were present in the markdown.

Three bugs caused this:
1. The threat-level regex expected plain text in table cells (`| ChatGPT | HIGH |`) but the agent output used bold markdown (`| **ChatGPT** | HIGH |`) and dot-based confidence (`●●●`)
2. The section-matching logic searched for keywords in the full section body, not just the header — so the "API & Models Intelligence" section matched as "Codex" because it contained the word "Codex" in its body text when discussing competitive positioning
3. The "C-Suite Dashboard" section matched as "Sources" because it cited source URLs

**Impact**: The HTML dashboard would have been empty in 3 of its most important sections. This would have been caught before delivery, but only because we tested the full pipeline — if we had skipped end-to-end testing, the emailed report would have been incomplete.

**Fix**: Rewrote the parser to (1) handle bold markdown and dot-based confidence in regex patterns, (2) match section keywords against the header line only (not body text), and (3) exclude "knowledge" from the "sources" keyword match. After fixing, the parser correctly extracted: 3 threat levels, 3 must-know items, 6 ChatGPT signals, 6 Codex signals, 7 API signals, 4 horizon signals, and 26 sources.

### Failure 6: Threat Levels Are Per-Section, Not Per-Competitor
**What happened**: In our LLM-as-judge evaluation (10 scenarios, Claude as judge, 5 scoring dimensions), the agent scored 8.64/10 overall — but the weakest dimension was Threat-Level Accuracy (8.30/10). Two scenarios scored 5/10 and 6/10 on this dimension because the agent assigns threat levels at the *product line* level (ChatGPT=HIGH, Codex=HIGH, API=HIGH) but cannot distinguish threat levels for *individual competitors* within the same section.

For example, xAI's $20B funding and X algorithm integration warranted a MEDIUM threat to ChatGPT (speculative, not shipped, co-founder departures suggest execution risk), but the agent rated the entire ChatGPT section as HIGH because Anthropic's 14+ launches and Google's migration tool were genuinely HIGH. xAI's MEDIUM got lost inside the section-level HIGH. Similarly, Cognition's integration challenges warranted MEDIUM for Codex, but Cursor's $29.3B raise drove the section to HIGH.

**Impact**: Decision-makers see "ChatGPT = HIGH" and cannot distinguish between "Anthropic is a HIGH threat that needs immediate response" and "xAI is a MEDIUM threat to monitor." Every competitor in a section gets the same urgency level, which dilutes the signal for less-urgent-but-still-notable threats.

**Fix (partial)**: This is a design limitation we identified but did not fully resolve in v1.1. The C-Suite Dashboard shows section-level threat ratings, and individual findings within sections are implicitly ranked by order and detail. A v1.2 fix would add per-competitor threat indicators within each section, or at minimum a "primary driver" label on the Dashboard (e.g., "ChatGPT: HIGH — driven by Anthropic + Google; xAI: MEDIUM").

### Failure 7: Source Citation Inconsistency
**What happened**: The LLM-as-judge evaluation scored Source Citation at 7.40/10 — the joint-lowest dimension. The agent cites sources for some findings (e.g., "(Bloomberg, Google Blog)" inline) but presents other critical statistics without attribution in the body text. The most notable example: "Chinese models now account for 61% of total token consumption on OpenRouter" — a key data point that appears in the C-Suite Dashboard, API section, and multiple other locations — has no inline source citation. The IndexBox and TeamDay sources appear in the Sources footer but aren't linked to this specific claim.

**Impact**: A reader scanning the API section cannot verify the 61% claim without scrolling to the bottom and guessing which source covers it. For an executive audience, unattributed quantitative claims reduce trust — especially when the number is central to a threat-level rating.

**Fix (partial)**: Added source attribution for most signals in the report. However, consistent inline citation for *every* quantitative claim remains an open issue. A v1.2 fix would enforce a rule in the prompt: "Every sentence containing a number, percentage, or ranking must include an inline source citation in parentheses."

---

## Appendix A: Evaluation Results Summary

We evaluated the agent's real weekly report output (`prior_reports/week_of_2026-03-23.md`) using LLM-as-judge with 10 test scenarios covering all product lines and competitor types. Full results in `eval/eval_results.md`.

### Scoring Dimensions

| Dimension | Weight | Avg Score /10 |
|-----------|--------|-------------|
| Signal Detection | 30% | **9.50** |
| Product-Line Classification | 20% | **9.60** |
| Threat-Level Accuracy | 20% | **8.30** |
| Source Citation | 15% | **7.40** |
| Actionability | 15% | **7.40** |

### Per-Scenario Scores

| # | Scenario | Weighted Score |
|---|----------|---------------|
| 1 | Anthropic Mythos Leak | 8.35 |
| 2 | Google Migration Tool | 8.60 |
| 3 | Cursor $29.3B + Automations | **9.20** (highest) |
| 4 | Google Jules GA | 8.60 |
| 5 | DeepSeek V4 Release | 8.55 |
| 6 | Chinese Models 61% OpenRouter | 8.65 |
| 7 | Zhipu GLM-5 Coding | 8.90 |
| 8 | Perplexity Platform Evolution | **9.30** (highest) |
| 9 | xAI $20B + X Algorithm | **7.40** (lowest) |
| 10 | Cognition Integration Status | 8.85 |
| | **Overall Average** | **8.64 / 10** |

### Key Evaluation Findings

- **Zero missed signals**: The agent detected all 10 competitive signals with zero keywords missing across all scenarios
- **Near-perfect classification**: 9.60/10 average — all signals routed to the correct product-line section
- **Threat-level granularity gap**: Per-section ratings (HIGH/MEDIUM/LOW) cannot distinguish per-competitor threat levels (Failures 6 above)
- **Citation inconsistency**: Quantitative claims sometimes lack inline attribution (Failure 7 above)
- **Actionability strongest for structural shifts**: Platform pivots (Perplexity: 9/10) and integration risks (Cognition: 9/10) are framed well; funding announcements (xAI: 6/10) lack concrete implications

---

## Appendix B: Project Structure

```
competitor-intel-agent/
├── SUBMISSION.md                          ← This file (final deliverable)
├── README.md                              ← Project overview and setup instructions
├── knowledge_base/
│   ├── openai_context.md                  ← OpenAI products, strategy, metrics
│   ├── competitor_profiles.md             ← 20+ competitors organized by product line
│   └── industry_benchmarks.md             ← LMSYS Arena, SWE-Bench, pricing tables
├── prompts/
│   ├── agent_system_prompt.md             ← Full agent prompt (Section 2)
│   └── prompt_log.md                      ← Prompt iteration history (v1.0, v1.1)
├── scripts/
│   ├── run_agent.sh                       ← Full pipeline orchestrator (Steps 0-7)
│   ├── exa_scan.py                        ← Exa API pre-scan (24 queries, 5 sections)
│   ├── generate_report.py                 ← Markdown → styled HTML converter
│   └── send_report.py                     ← PDF generation (Playwright) + email (Resend)
├── prior_reports/
│   ├── week_of_2026-03-23.md              ← Real weekly report (26 sources, 17KB)
│   ├── daily_2026-03-29.md                ← Daily alert template (3 RED, 2 YELLOW)
│   └── exa_scan_2026-03-29.md             ← Exa scan output (95 signals, 42KB)
├── report_output/
│   ├── openai_intel_report.html           ← Hand-crafted HTML dashboard template
│   ├── week_of_2026-03-23.html            ← Generated HTML from real agent output
│   ├── openai_intel_report.pdf            ← PDF of template (288KB)
│   └── week_of_2026-03-23.pdf             ← PDF of generated report (216KB)
└── eval/
    ├── README.md                          ← Eval framework documentation
    ├── test_scenarios.json                ← 10 test scenarios with ground truth
    ├── run_eval.py                        ← LLM-as-judge evaluation script
    └── eval_results.md                    ← Evaluation results (8.64/10 avg)
```

## Appendix C: Prompt Iteration History

| Version | Date | Author | Key Changes |
|---------|------|--------|-------------|
| v1.0 | March 28, 2026 | David | Initial prompt. Flat Tier 1/2/3 competitor structure. 6 data sources. ~10 Twitter accounts. |
| v1.1 | March 29, 2026 | Jack | Product-line-first competitor structure (ChatGPT/Codex/API). 7 data sources (+leaderboard monitoring). 30+ Twitter accounts. Exa API connected. Twitter noise filtering added. Knowledge base staleness safeguard ("always trust live data") added. |

Full prompt iteration details with design rationale in `prompts/prompt_log.md`.

## Appendix D: Project Team & Workflow

- **David & Jack**: Competitor Intelligence Agent (design, prompt engineering, output formatting, pipeline implementation)
- **Tatsuro & Ez**: Evaluation Agent (evaluation framework, scoring rubric, automated testing)

### Build Process

David built the v1.0 first draft on Saturday March 28. Jack reviewed and substantially upgraded on Sunday March 29 in a single session — restructuring competitors by product line, adding 20+ new competitors, connecting Exa API, building the email/PDF pipeline, running a full test with live web search, finding and fixing 18 bugs, and running the LLM-as-judge evaluation. Full session log in `conversation_log_jack.md` (16 decisions, 18 bugs found).
