#!/bin/bash
# ============================================================
# OpenAI Competitor Intelligence Agent — Runner Script
# ============================================================
# Usage: ./scripts/run_agent.sh
#
# Prerequisites:
#   - Claude Code installed: npm install -g @anthropic-ai/claude-code
#   - ANTHROPIC_API_KEY set in environment
#   - (Optional) EXA_API_KEY set for Exa search
# ============================================================

set -e

# Colors for output
BOLD='\033[1m'
DIM='\033[2m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m'

# Get project root (parent of scripts/)
PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TODAY=$(date +%Y-%m-%d)
WEEK_START=$(date -d "last monday" +%Y-%m-%d 2>/dev/null || date -v-mon +%Y-%m-%d 2>/dev/null || echo "$TODAY")

echo -e "${BOLD}╔══════════════════════════════════════════════════╗${NC}"
echo -e "${BOLD}║  OpenAI Competitive Intelligence Agent v1.0     ║${NC}"
echo -e "${BOLD}╚══════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${DIM}Date: ${TODAY}${NC}"
echo -e "${DIM}Project: ${PROJECT_ROOT}${NC}"
echo ""

# Check prerequisites
if ! command -v claude &> /dev/null; then
    echo -e "${YELLOW}⚠ Claude Code not found. Install with: npm install -g @anthropic-ai/claude-code${NC}"
    exit 1
fi

if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo -e "${YELLOW}⚠ ANTHROPIC_API_KEY not set. Export it first:${NC}"
    echo "  export ANTHROPIC_API_KEY=your_key_here"
    exit 1
fi

echo -e "${GREEN}✓ Prerequisites met${NC}"
echo ""

# Build the user message
USER_MESSAGE="Generate the weekly competitive intelligence report for OpenAI.

Today's date is ${TODAY}. The reporting week is ${WEEK_START} to ${TODAY}.

STEP 1: Read the knowledge base files and Exa scan for context:
- knowledge_base/openai_context.md (OpenAI products & strategy)
- knowledge_base/competitor_profiles.md (competitors organized by product line)
- knowledge_base/industry_benchmarks.md (Arena rankings, SWE-bench, pricing)
- prior_reports/exa_scan_${TODAY}.md (pre-fetched Exa semantic search signals — USE THIS as primary input)

STEP 2: Check prior_reports/ for any previous reports to enable trend detection.

STEP 3: Use web search to gather current competitive signals BY PRODUCT LINE:

ChatGPT (consumer):
- Search Anthropic Claude, Google Gemini, xAI Grok, Perplexity for consumer product news
- Search Twitter/X for executive posts (Dario Amodei, Sundar Pichai, Elon Musk, Aravind Srinivas)
- Search Reddit (r/ChatGPT, r/ClaudeAI) and HN for user sentiment

Codex (coding tools):
- Search Cursor, Claude Code, Gemini Code Assist, GitHub Copilot, Cognition (Devin + Windsurf) for feature launches
- Search career pages for hiring signals in engineering/product roles
- Search GitHub, Reddit (r/LocalLLaMA), HN for developer sentiment and tool adoption

API & Models (platform):
- Search for new model releases and pricing changes from closed-source APIs (Anthropic, Google, xAI, Mistral)
- Search for open-source model activity (DeepSeek, Qwen, Zhipu/GLM, Moonshot/Kimi, MiniMax, Meta/LLaMA)
- Search for partnership and infrastructure announcements

STEP 3b: Check leaderboards and marketplace rankings:
- LMSYS Chatbot Arena (lmarena.ai) — check for Elo rank changes vs. knowledge_base/industry_benchmarks.md baselines
- OpenRouter rankings (openrouter.ai/rankings) — check token usage shifts, new model entries, pricing changes
- HuggingFace Open LLM Leaderboard — check for new frontier open-source models
- SWE-Bench Verified (swebench.com) — check for coding benchmark changes (critical for Codex section)

STEP 4: Synthesize findings into the structured report format defined in the system prompt.

STEP 5: Save the report as a markdown file in prior_reports/week_of_${WEEK_START}.md

Format every finding as: **Company Name** — Description of the signal"

# Step 0: Run Exa semantic search scan (pre-fetches signals for agent context)
echo -e "${BOLD}Running Exa intelligence scan...${NC}"
python3 "${PROJECT_ROOT}/scripts/exa_scan.py" --days 7
EXA_SCAN="${PROJECT_ROOT}/prior_reports/exa_scan_$(date +%Y-%m-%d).md"
echo ""

echo -e "${BOLD}Starting agent...${NC}"
echo ""

# Run Claude Code with the system prompt
claude --system-prompt "${PROJECT_ROOT}/prompts/agent_system_prompt.md" \
  --allowedTools "WebSearch,Read,Write" \
  "${USER_MESSAGE}"

echo ""
echo -e "${GREEN}✓ Agent run complete${NC}"
echo -e "${DIM}Check prior_reports/ for the generated report${NC}"

# Step 6: Generate HTML from markdown and email the report
REPORT_MD="${PROJECT_ROOT}/prior_reports/week_of_${WEEK_START}.md"
REPORT_HTML="${PROJECT_ROOT}/report_output/week_of_${WEEK_START}.html"

if [ -f "$REPORT_MD" ]; then
    echo ""
    echo -e "${BOLD}Generating HTML report...${NC}"
    python3 "${PROJECT_ROOT}/scripts/generate_report.py" "$REPORT_MD" -o "$REPORT_HTML"

    if [ -f "$REPORT_HTML" ]; then
        echo ""
        echo -e "${BOLD}Emailing report...${NC}"
        python3 "${PROJECT_ROOT}/scripts/send_report.py" "$REPORT_HTML"
    else
        echo -e "${YELLOW}⚠ HTML generation failed — skipping email${NC}"
    fi
else
    echo -e "${YELLOW}⚠ Report markdown not found at ${REPORT_MD} — skipping HTML/email${NC}"
fi

echo ""
echo -e "${DIM}Remember to update knowledge_base/competitor_profiles.md with new findings${NC}"
