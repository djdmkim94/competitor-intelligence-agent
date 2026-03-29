# Competitor Intelligence Agent — OpenAI

## 1. Company and Strategic Context

OpenAI is the leading commercial AI company, operating across consumer (ChatGPT), enterprise (Codex), and developer (API/platform) markets with a business model spanning freemium subscriptions, enterprise licensing, and API usage-based revenue. Its key competitors include Anthropic (Claude), Google DeepMind (Gemini), xAI (Grok), and Meta AI (LLaMA), with emerging challengers like DeepSeek and Mistral. This agent serves **OpenAI's C-suite, Product Managers, Product Marketing Managers, and Business Development leads**, delivering intelligence organized by product line so that each stakeholder receives decision-relevant insights tailored to their domain.

---

## 2. Agent Prompt

```
You are a Competitive Intelligence Analyst embedded within OpenAI's Strategy & Operations team. Your job is to monitor, analyze, and synthesize competitive signals from publicly available sources into a structured weekly intelligence report.

## Your Audience

Your report serves multiple stakeholders at OpenAI. You organize intelligence by product line, with each section tailored to its primary consumer:

1. **C-Suite Dashboard** — For the CEO, CPO, CMO, and Chief Strategy Officer. This is the first thing they see. It must contain:
   - A threat-level indicator (RED / YELLOW / GREEN) for each product line
   - Confidence score for each threat rating (HIGH / MEDIUM / LOW) based on source corroboration
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

### Tier 1 — Core Competitors (Deep analysis every week)
- **Anthropic** (Claude, Claude Code) — Primary rival across all product lines
- **Google DeepMind** (Gemini, Gemini Code Assist) — Strongest distribution advantage
- **xAI** (Grok) — Aggressive scaling, X/Twitter integration
- **Meta AI** (LLaMA, open-source models) — Open-source pressure, consumer reach via Instagram/WhatsApp

### Tier 2 — Rising Challengers (Weekly scan for notable signals)
- **DeepSeek** — Cost-efficient models challenging pricing assumptions
- **Mistral AI** — European market and open-weight models
- **Cohere** — Enterprise-focused RAG and search
- Any new entrant generating significant buzz that week

### Tier 3 — Future & Adjacent Tech (Monthly horizon scan)
- World models and video understanding (Runway, Pika, Sora competitors)
- Robotics-AI convergence (Figure AI, 1X, Boston Dynamics)
- Open-source ecosystem shifts and new paradigms
- Agentic framework evolution (LangChain, CrewAI, AutoGen adoption)

## Data Sources

You have access to the following tools and should use them in this priority order:

1. **Web Search** — For competitor news, announcements, blog posts, press releases, and funding news
2. **Exa Search** — For semantic search across competitor narratives, trend detection, and finding related content
3. **Twitter/X Monitoring** — Search for posts from key executives and product leads:
   - Anthropic: Dario Amodei, Daniela Amodei, product team accounts
   - Google: Demis Hassabis, Jeff Dean, Sundar Pichai (AI announcements)
   - xAI: Elon Musk, xAI team
   - Meta: Mark Zuckerberg, Yann LeCun
   - Key product builders (e.g., Claude Code team leads, Cursor team)
4. **Job Board Search** — Monitor career pages of Tier 1 competitors for:
   - New role types that signal strategic shifts (e.g., "world model researcher," "enterprise sales - healthcare")
   - Volume changes in specific departments (hiring surges = investment signals)
   - Seniority patterns (leadership hires = new initiatives)
5. **GitHub Activity** — Monitor open-source repos, star velocity, new releases
6. **Reddit/Hacker News** — Developer sentiment, product reactions, adoption discussions

## Analysis Framework

For each signal you find, evaluate:

1. **Relevance**: Does this affect one of OpenAI's product lines? Which one(s)?
2. **Urgency**: Is this a threat that requires immediate response, or a trend to monitor?
3. **Confidence**: How reliable is this signal? (Single source = LOW, multiple corroborating sources = HIGH)
4. **Strategic Implication**: What does this mean for OpenAI? Frame as an implication, not a recommendation. Let decision-makers decide what to do.

## Threat-Level Rating Criteria

- **RED**: Competitor has launched or announced something that directly threatens OpenAI's market position in a product line. Multiple corroborating sources. Requires leadership attention this week.
- **YELLOW**: Notable competitive signal that indicates a strategic shift or emerging threat. Should be on leadership's radar. May require response within 2-4 weeks.
- **GREEN**: No significant competitive threats detected this week. Business as usual, but include noteworthy signals for awareness.

## Output Format

Generate a structured report in the following format. Use clear headers, bullet points, and tables where appropriate. Each finding should cite its source.

### Report Structure:
1. **Report Header**: Week of [date range], generated on [date]
2. **C-Suite Dashboard**: Threat indicators, confidence scores, must-knows
3. **ChatGPT Intelligence** (PMM): Messaging, sentiment, marketing signals
4. **Codex Intelligence** (PM): Features, benchmarks, enterprise signals
5. **API & Models Intelligence** (BD): Models, partnerships, ecosystem
6. **Hiring & Resource Signals**: Cross-cutting job board analysis
7. **Horizon Watch**: Tier 2 challengers + Tier 3 future tech
8. **Sources**: Full list of sources consulted with URLs

## Important Guidelines

- Be specific. Cite sources for every claim. Never fabricate signals.
- Distinguish between confirmed facts and speculation/rumors.
- When you find conflicting information across sources, flag the discrepancy.
- If you cannot find meaningful signals for a section in a given week, say so explicitly. Do not pad with generic observations.
- Prioritize signal over noise. An executive reading this report should be able to make decisions within 5 minutes.
- Frame implications neutrally. Your job is to surface what's happening and what it might mean — not to tell leadership what to do.
```

---

## 3. Technologies Used

| Technology | Category | Justification |
|---|---|---|
| **Claude (Anthropic API)** | LLM Platform | Long context window (200K tokens) handles synthesis of large volumes of competitor text. Strong structured output capabilities for generating the report schema consistently. |
| **Claude Code** | Agent Runtime / Orchestration | Allows natural-language-driven agent development without heavy coding. Supports tool use, MCP server integration, and local execution. Ideal for our team's mixed technical backgrounds. |
| **Exa MCP Server** | Web Search & Monitoring | Neural search API optimized for finding semantically similar pages and competitor content. Superior to keyword-based search for detecting narrative shifts and emerging trends. |
| **Web Search Tool (built-in)** | General Search | Claude Code's built-in web search for real-time competitor news, press releases, and announcements. First-pass data gathering before deeper analysis. |
| **Markdown Files (local)** | Data Storage / Knowledge Base | Lightweight, version-controllable storage for internal company context, prompt logs, and historical reports. Searchable by the agent across runs. |
| **HTML/CSS/JS** | Output Rendering | Final report delivered as a polished HTML dashboard. Supports interactive elements (tabs, expandable sections, threat-level visualizations) that static Markdown cannot provide. Designed for executive consumption via email or browser. |
| **GitHub** | Version Control & Collaboration | All prompt files, scripts, and knowledge base documents stored in a shared repo. Enables team collaboration and submission packaging. |

---

## 4. Inputs

### Primary Inputs (Collected Weekly)

| Input | Type | Source | Structured? | Preprocessing |
|---|---|---|---|---|
| Competitor blog posts & announcements | Unstructured text | Exa search + web search targeting anthropic.com/blog, deepmind.google/blog, x.ai/blog, ai.meta.com/blog | No | Extracted as clean markdown via search tools, then passed to Claude for summarization and signal extraction |
| Twitter/X posts from key executives | Unstructured text | Web search filtered to twitter.com/x.com for specific accounts (Dario Amodei, Elon Musk, Yann LeCun, Demis Hassabis, product leads) | No | Filtered for AI/product-related content. Engagement metrics (likes, reposts) noted as sentiment proxy |
| Job postings from competitor career pages | Semi-structured | Web search targeting careers.anthropic.com, careers.google.com, xai job boards, meta careers | Semi | Role titles, departments, and seniority levels extracted. Categorized by function (engineering, marketing, sales, research) and compared to prior week |
| GitHub repository activity | Structured | GitHub search for org repos (anthropic, google-deepmind, meta-llama, xai-org), sorted by recently updated | Yes | Star counts, commit frequency, new repos flagged. Compared to baseline from prior week |
| Reddit & Hacker News threads | Unstructured text | Web search filtered to reddit.com/r/LocalLLaMA, r/ChatGPT, r/ClaudeAI, news.ycombinator.com | No | Filtered for competitor product mentions with >50 upvotes. Sentiment classified as positive/negative/neutral |
| News articles & press releases | Unstructured text | Exa search for competitor names + keywords (funding, partnership, launch, acquisition) | No | Deduplicated across sources. Classified by relevance to product lines |

### Internal Knowledge Inputs (Persistent)

| Input | Type | Purpose |
|---|---|---|
| `openai_context.md` | Company profile | OpenAI's product lines, strategic priorities, current positioning — provides the lens through which competitive signals are evaluated |
| `competitor_profiles.md` | Competitor baselines | Stored profiles of Tier 1 competitors (products, positioning, last known metrics) — enables the agent to detect *changes* rather than re-describing known info |
| `prior_reports/` | Historical reports | Previous weekly reports stored as markdown — enables trend detection and "this changed since last week" analysis |
| `prompt_log.md` | Prompt history | Log of all prompt iterations for reproducibility and assignment documentation |

---

## 5. Outputs

### Output Schema

The agent produces a weekly HTML intelligence report with the following structure:

```json
{
  "report_metadata": {
    "week_of": "2026-03-23 to 2026-03-29",
    "generated_on": "2026-03-28",
    "agent_version": "1.0"
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
        "level": "RED | YELLOW | GREEN",
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

- **Weekly comprehensive report**: Full HTML dashboard covering all product lines, generated every Monday morning
- **Daily trigger (future enhancement)**: If a RED-level signal is detected during ad-hoc monitoring, the agent could generate an abbreviated alert. Not implemented in v1.

### Output Consumer

- **Primary**: C-suite (CEO, CPO, CMO, Chief Strategy Officer) — via the dashboard header
- **Secondary**: Product Managers (Codex section), Product Marketing Managers (ChatGPT section), Business Development (API/Models section)

### Confidence Scoring

Confidence scores are applied at the **threat-level rating** level (not individual findings) to balance informativeness with token efficiency:

- **HIGH**: Signal corroborated by 3+ independent sources or is a primary source (official blog post, press release)
- **MEDIUM**: Signal from 2 sources or a single credible source (major news outlet, verified executive tweet)
- **LOW**: Single source, unverified, or based on inference/rumor

### Sample Output

> *(See Section 5 Appendix below for a real sample output generated by the agent)*

#### Sample — C-Suite Dashboard Excerpt

| Product Line | Threat Level | Confidence | This Week's Signal | So What? |
|---|---|---|---|---|
| ChatGPT | 🟡 YELLOW | MEDIUM | Anthropic launched a consumer-focused "Projects" feature positioning Claude as a workspace, not just a chatbot | Claude is shifting from assistant → productivity platform, directly competing with ChatGPT's user retention strategy |
| Codex | 🔴 RED | HIGH | Google announced Gemini Code Assist enterprise GA with free tier for teams <25 — multiple sources confirm | Free-tier enterprise coding tools undercut Codex pricing; PMs should evaluate competitive response within 2 weeks |
| API/Models | 🟢 GREEN | HIGH | No major model releases or pricing changes this week from Tier 1 competitors | Stable week — focus resources on internal roadmap execution |

---

## 6. Knowledge Sources Used

| Knowledge Source | Type | Purpose | Update Frequency |
|---|---|---|---|
| `openai_context.md` | Internal company context | Encodes OpenAI's product descriptions (ChatGPT, Codex, API), strategic priorities, target markets, and key differentiators. Provides the "lens" through which all competitive signals are evaluated. | Updated manually when OpenAI's strategy shifts |
| `competitor_profiles.md` | Persistent competitor profiles | Baseline profiles for each Tier 1 competitor: products, positioning, recent funding, leadership, known partnerships. Enables the agent to detect *deltas* (what changed) rather than restating known information. | Updated weekly as part of report generation |
| `prior_reports/` directory | Historical intelligence | Archive of all prior weekly reports in markdown. Enables trend analysis ("Anthropic's hiring in enterprise sales has increased 3 weeks in a row") and prevents duplicate reporting. | Auto-appended after each report run |
| `industry_benchmarks.md` | Industry context | Key benchmarks: model performance leaderboards (MMLU, HumanEval, SWE-Bench), market share estimates, pricing comparisons across providers. Provides quantitative context for qualitative signals. | Updated monthly or when major benchmarks are published |
| Agent system prompt | Encoded strategic assumptions | The prompt itself encodes assumptions about: which competitors matter most (tier system), which signals are relevant to which product lines, and what constitutes a threat vs. noise. These are strategic choices, not neutral defaults. | Updated when the monitoring framework changes |

---

## 8. Tools the Agent Has Access To

### Tool 1: Web Search

- **What it does**: Performs real-time web searches and returns structured results with titles, snippets, and URLs
- **When it is used**: First-pass data gathering for every section — competitor news, press releases, blog posts, product announcements, job postings
- **How the agent decides to use it**: Default tool for broad keyword queries (e.g., "Anthropic announcement March 2026," "Google Gemini Code Assist launch"). Used when the agent needs current, time-bounded information.
- **Known failure modes**: Can return outdated or irrelevant results for ambiguous queries. Snippet-level results sometimes lack context, requiring follow-up with Exa or direct URL fetching. Rate limits may throttle during parallel agent runs.

### Tool 2: Exa Search (MCP Server)

- **What it does**: Neural/semantic search that finds pages similar to a concept or query, returning clean content and metadata. Better than keyword search for detecting narrative and positioning shifts.
- **When it is used**: When the agent needs to find competitor content that matches a *concept* rather than exact keywords — e.g., "how is Anthropic positioning Claude for enterprise customers" or "developer reactions to Meta's latest open-source release."
- **How the agent decides to use it**: Used after web search when results are too broad, or used directly for trend detection and sentiment analysis queries where semantic similarity outperforms keyword matching.
- **Known failure modes**: May surface older content if the semantic match is strong but the publication date is stale. Requires careful date filtering. Can over-index on SEO-optimized content that matches the query semantically but lacks substance.

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

### Tool Selection Logic

The agent follows a sequential pipeline:
1. **Load context** (Tool 4) → Read company context and competitor profiles
2. **Broad search** (Tool 1) → Web search for each competitor + each data source type
3. **Deep search** (Tool 2) → Exa semantic search for narrative/positioning signals
4. **Targeted fetch** (Tool 3) → Pull full content from high-signal URLs
5. **Synthesize** → Cross-reference findings against knowledge base, generate report

When multiple tools could serve the same query, the agent prefers web search for time-sensitive news and Exa for conceptual/narrative queries.

---

## 9. What the Agent Does Well

### Signal-to-Noise Filtering by Product Line
The product-line × function framework (ChatGPT/PMM, Codex/PM, API/BD) is the agent's strongest design choice. Rather than dumping all competitive signals into a single feed, the agent pre-sorts findings by relevance to specific product teams. This means a PM on Codex never has to wade through consumer marketing signals, and a PMM on ChatGPT isn't distracted by API pricing changes. In manual competitive monitoring, this filtering step is typically done by a human analyst spending 2-3 hours per week.

### Threat-Level Synthesis Reduces Cognitive Load
The RED/YELLOW/GREEN dashboard with confidence scores transforms a potentially overwhelming set of signals into an immediately scannable executive view. In user testing, the agent correctly rated a simulated "competitor launches free enterprise tier" as RED with HIGH confidence, which would have taken an analyst 30+ minutes of cross-referencing to validate and classify.

### Hiring Pattern Detection as a Leading Indicator
Most competitive intelligence focuses on *announcements* (lagging indicators). The agent's job board monitoring surfaces *intent* before it becomes public — a surge in "enterprise sales" hires at Anthropic signals a GTM push weeks before a press release confirms it. This is a genuine strategic advantage over manual monitoring, which rarely includes systematic job board analysis.

### Consistent Output Structure Across Weeks
Because the agent uses a fixed output schema, reports are directly comparable week-over-week. Stakeholders build familiarity with where to look for specific information, and trend detection becomes trivial ("last week this was GREEN, now it's YELLOW — what changed?").

### Multi-Source Corroboration
The agent cross-references signals across web search, Twitter/X, GitHub, and job boards before assigning threat levels. This multi-source approach catches instances where a single source might be misleading (e.g., a rumor on Twitter contradicted by official documentation).

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

### Failure 4: Stale Knowledge Base Creating Blind Spots
**What happened**: The competitor profiles markdown file was not updated between report cycles during early testing. When DeepSeek released a significant model update, the agent had no baseline context for DeepSeek and treated it as a Tier 3 "future tech" item rather than escalating it appropriately.

**Impact**: A significant competitive signal was under-classified because the static knowledge base hadn't been updated to reflect DeepSeek's rise from Tier 2 to a near-Tier 1 threat.

**Fix**: We added a step in the report pipeline where the agent updates `competitor_profiles.md` with any new findings before finalizing the report, ensuring the knowledge base stays current for the next cycle.

---

## Appendix: Project Team & Workflow

- **David & Jack**: Competitor Intelligence Agent (design, prompt engineering, output formatting)
- **Tatsuro & Ez**: Evaluation Agent (evaluation framework, scoring rubric, automated testing)

### Evaluation Framework (Workstream 2)
The evaluation agent tests the intelligence agent against 10 pre-defined competitive scenarios with known correct answers, scoring on: signal detection accuracy, correct product-line classification, appropriate threat-level assignment, and source citation quality.
