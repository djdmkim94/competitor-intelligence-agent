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

STEP 1: Read the knowledge base files for context:
- knowledge_base/openai_context.md
- knowledge_base/competitor_profiles.md
- knowledge_base/industry_benchmarks.md

STEP 2: Check prior_reports/ for any previous reports to enable trend detection.

STEP 3: Use web search to gather current competitive signals:
- Search for each Tier 1 competitor (Anthropic, Google Gemini, xAI, Meta AI) + news/announcements/launches
- Search for competitor career pages for hiring signals
- Search Twitter/X for key executive posts about AI products
- Search GitHub for notable open-source activity
- Search Reddit (r/ChatGPT, r/ClaudeAI, r/LocalLLaMA) and Hacker News for developer sentiment

STEP 4: Synthesize findings into the structured report format defined in the system prompt.

STEP 5: Save the report as a markdown file in prior_reports/week_of_${WEEK_START}.md

Format every finding as: **Company Name** — Description of the signal"

echo -e "${BOLD}Starting agent...${NC}"
echo ""

# Run Claude Code with the system prompt
claude --system-prompt "${PROJECT_ROOT}/prompts/agent_system_prompt.md" \
  --allowedTools "WebSearch,Read,Write" \
  "${USER_MESSAGE}"

echo ""
echo -e "${GREEN}✓ Agent run complete${NC}"
echo -e "${DIM}Check prior_reports/ for the generated report${NC}"
echo -e "${DIM}Remember to update knowledge_base/competitor_profiles.md with new findings${NC}"
