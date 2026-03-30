# Prompt Log

> Log every prompt iteration here. This is required for the assignment deliverable.

---

## v1.0 — March 28, 2026 (David)

**What changed**: Initial prompt created.

**Key design decisions**:
- Organized by product line × function (ChatGPT/PMM, Codex/PM, API/BD) rather than by competitor
- Three-tier competitor framework (Core, Rising, Future)
- Threat levels are HIGH/MEDIUM/LOW (not red/yellow/green) with confidence dots
- All findings formatted as "Company — Signal" for scanability
- Implications framed neutrally (no prescriptive recommendations)
- Confidence scoring only on threat-level ratings (not every finding) to manage token cost

**Prompt file**: `prompts/agent_system_prompt.md`

**Result**: Successfully generates structured report. See `report_output/openai_intel_report.html` for sample.

**Known issues**:
- Agent sometimes pads quiet sections with generic observations instead of saying "no signals"
- Twitter/X search occasionally surfaces personal tweets from execs alongside product signals
- LinkedIn scraping not feasible — pivoted to career pages directly

---

## v1.1 — March 29, 2026 (Jack)

**What changed**: Major restructure of the "Competitors to Monitor" section from flat Tier 1/2/3 → product-line-first organization.

**Key design decisions**:
- Competitors now organized by product line (ChatGPT, Codex, API & Models) instead of flat tiers
- Each report section has its own focused competitor set rather than filtering one giant list
- API competitors split into closed-source and open-source categories
- Added 10+ new competitors: Perplexity, Cursor, Cognition (Devin + Windsurf), GitHub Copilot, Zhipu AI (GLM-5), Alibaba/Qwen, Moonshot/Kimi, MiniMax, ByteDance, NVIDIA Nemotron
- Merged Windsurf into Cognition (post-acquisition)
- Added key market signals: Chinese models = 61% of OpenRouter tokens, programming = 50%+ of API usage
- Added Twitter accounts for Cursor team (Michael Truell), Cognition (Scott Wu), Perplexity (Aravind Srinivas)
- Updated Data Sources section to include new monitoring targets

**Rationale**: The competitive landscape differs significantly by product line. A flat tier system forced the agent to filter irrelevant competitors per section, leading to noise. Product-line-first means each stakeholder sees only their relevant competitors.

**Prompt file**: `prompts/agent_system_prompt.md`

**Result**: Prompt tested with live web search — generated full weekly + daily reports. 10 knowledge base staleness bugs found and fixed during test. Parser bugs in generate_report.py fixed. Email pipeline (Resend + PDF) built and tested.

**Known issues**:
- Exa MCP still not connected — semantic search for narrative shifts would improve ChatGPT section
- No first-run handling (prompt assumes prior reports exist for delta detection)
- Threat level format inconsistency (HIGH/MEDIUM/LOW in prompt vs 🔴🟡🟢 in SUBMISSION sample)
- Daily report format not yet defined in system prompt (template exists in prior_reports/)
- Agent has not been tested with the new product-line structure yet

---

## v1.2 — [DATE] ([NAME])

**What changed**: [describe changes]

**Prompt file**: `prompts/agent_system_prompt.md`

**Result**: [what happened]

---
