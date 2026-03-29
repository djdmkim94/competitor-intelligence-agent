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

## v1.1 — [DATE] ([NAME])

**What changed**: [describe changes]

**Prompt file**: `prompts/agent_system_prompt.md`

**Result**: [what happened]

---
