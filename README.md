# OpenAI Competitor Intelligence Agent

## Team
- **David & Jack** — Intelligence Agent (design, prompt engineering, output)
- **Tatsuro & Ez** — Evaluation Agent (scoring framework, automated testing)

## Project Structure

```
competitor-intel-agent/
├── README.md                          ← You are here
├── SUBMISSION.md                      ← Final markdown submission (all 10 sections)
├── report_output/
│   └── openai_intel_report.html       ← Sample HTML report output
├── knowledge_base/
│   ├── openai_context.md              ← OpenAI's products, strategy, priorities
│   ├── competitor_profiles.md         ← Tier 1-3 competitor baselines
│   └── industry_benchmarks.md         ← Model leaderboards, pricing, market data
├── prior_reports/
│   └── (weekly reports saved here after each run)
├── prompts/
│   ├── agent_system_prompt.md         ← The full agent prompt (Section 2)
│   └── prompt_log.md                  ← Log of all prompt iterations
├── scripts/
│   ├── run_agent.sh                   ← One-command agent runner
│   └── generate_report.py            ← Python script to format HTML output
└── eval/
    └── (Tatsuro & Ez's evaluation framework goes here)
```

## Quick Start

### Prerequisites
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed (`npm install -g @anthropic-ai/claude-code`)
- Anthropic API key set: `export ANTHROPIC_API_KEY=your_key`
- (Optional) Exa API key: `export EXA_API_KEY=your_key`

### Run the Agent

```bash
# Option 1: One-command run
chmod +x scripts/run_agent.sh
./scripts/run_agent.sh

# Option 2: Run directly with Claude Code
claude-code --system-prompt prompts/agent_system_prompt.md \
  "Generate the weekly competitive intelligence report for OpenAI. \
   Today's date is $(date +%Y-%m-%d). \
   Read the knowledge base files in knowledge_base/ for context. \
   Output a structured report following the schema in the system prompt."
```

### After Running
1. Review the generated report
2. Save a copy to `prior_reports/week_of_YYYY-MM-DD.md`
3. Update `knowledge_base/competitor_profiles.md` with any new findings
4. Log the prompt used in `prompts/prompt_log.md`

## How to Edit & Contribute

### For Jack (Data Sources)
- Review and update `knowledge_base/competitor_profiles.md` — add any competitors or sources I missed
- Review `knowledge_base/openai_context.md` — make sure OpenAI's product descriptions are accurate
- Add specific Twitter/X accounts to monitor in the agent prompt

### For Tatsuro & Ez (Evaluation)
- Create your evaluation framework in the `eval/` directory
- The agent's output schema is defined in `SUBMISSION.md` Section 5
- Suggested approach: 10 test scenarios with known-correct answers, score on signal detection accuracy, threat-level assignment, and source citation quality

### For Everyone
- All prompt changes should be logged in `prompts/prompt_log.md`
- If you change the agent prompt, update both `prompts/agent_system_prompt.md` AND `SUBMISSION.md` Section 2

## Submission Checklist
- [ ] All 10 sections present in SUBMISSION.md
- [ ] Agent prompt is complete and not summarized
- [ ] At least one real sample output included
- [ ] At least one concrete failure example in Section 10
- [ ] Technologies justified (not just listed)
- [ ] HTML report renders correctly
- [ ] Prompt log shows iteration history

## Timeline
- **Saturday night**: First draft (David)
- **Sunday morning**: Jack reviews data sources & knowledge base
- **Monday 12pm Taiwan / 6pm Berkeley**: Team sync (optional)
- **Tuesday 5pm Berkeley / Wednesday 8am Taiwan**: Final submission
