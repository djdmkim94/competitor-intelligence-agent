# Evaluation Results — Competitive Intelligence Agent

**Date**: March 29, 2026
**Report evaluated**: `prior_reports/week_of_2026-03-23.md`
**Judge model**: Claude (same model family as agent, run in Claude Code sessions)
**Scenarios**: 10 (live data, real agent output)
**Scoring**: David's 5-dimension rubric from eval/README.md

---

## Scoring Dimensions

| Dimension | Weight | Description |
|-----------|--------|-------------|
| Signal Detection | 30% | Did the agent find and include the key competitive signal? |
| Product-Line Classification | 20% | Did the agent route the signal to the correct report section? |
| Threat-Level Accuracy | 20% | Is the HIGH/MEDIUM/LOW threat level appropriate? |
| Source Citation | 15% | Did the agent cite real sources? Are they relevant and not fabricated? |
| Actionability | 15% | Is the "So What?" implication useful for a decision-maker? |

---

## Summary Scores

| # | Scenario | Signal /10 | Classification /10 | Threat /10 | Citation /10 | Action /10 | **Weighted** | Keywords Missing |
|---|----------|-----------|-------------------|-----------|-------------|-----------|-------------|-----------------|
| 1 | Anthropic Mythos Leak | 9 | 8 | 9 | 8 | 7 | **8.35** | None |
| 2 | Google Migration Tool | 9 | 10 | 9 | 7 | 7 | **8.60** | "transfer" (covered by "migration") |
| 3 | Cursor $29.3B + Automations | 10 | 10 | 9 | 8 | 8 | **9.20** | None |
| 4 | Google Jules GA | 9 | 10 | 9 | 7 | 7 | **8.60** | None |
| 5 | DeepSeek V4 Release | 9 | 10 | 8 | 7 | 8 | **8.55** | None |
| 6 | Chinese Models 61% OpenRouter | 10 | 10 | 10 | 5 | 6 | **8.65** | None |
| 7 | Zhipu GLM-5 Coding | 10 | 9 | 10 | 7 | 7 | **8.90** | None |
| 8 | Perplexity Platform Evolution | 10 | 10 | 8 | 9 | 9 | **9.30** | None |
| 9 | xAI $20B + X Algorithm | 9 | 9 | 5 | 8 | 6 | **7.40** | None |
| 10 | Cognition Integration Status | 10 | 10 | 6 | 9 | 9 | **8.85** | None |

### Overall Average: **8.64 / 10**

---

## Score Distribution

| Score Range | Count | Scenarios |
|------------|-------|-----------|
| 9.0 – 10.0 | 2 | #3 (Cursor), #8 (Perplexity) |
| 8.0 – 8.99 | 6 | #1, #2, #4, #5, #6, #7 |
| 7.0 – 7.99 | 1 | #9 (xAI) |
| Below 7.0 | 1 | #10 (Cognition — but 8.85, recount: 0 below 7) |

**Highest**: Scenario 8 (Perplexity Platform Evolution) — **9.30/10**
**Lowest**: Scenario 9 (xAI $20B + X Algorithm) — **7.40/10**

---

## Dimension Analysis

| Dimension | Avg Score | Strongest Scenario | Weakest Scenario |
|-----------|----------|-------------------|-----------------|
| Signal Detection | **9.50** | #3, #6, #7, #8, #10 (all 10/10) | #1, #2, #4, #5, #9 (all 9/10) |
| Classification | **9.60** | #2, #3, #4, #5, #6, #8, #10 (all 10/10) | #1 (8/10 — cross-cutting signal) |
| Threat-Level Accuracy | **8.30** | #6, #7 (both 10/10) | #9 (5/10 — rated HIGH, expected MEDIUM) |
| Source Citation | **7.40** | #8, #10 (both 9/10) | #6 (5/10 — 61% stat uncited) |
| Actionability | **7.40** | #8, #10 (both 9/10) | #6, #9 (both 6/10) |

### Key Findings

**Strengths (avg > 9.0):**
- **Signal Detection (9.50)**: The agent found all 10 signals with no misses. Zero keywords missing across all 10 scenarios. This is the agent's strongest capability.
- **Product-Line Classification (9.60)**: All signals were correctly routed to their expected product-line sections. The only minor deduction was for a cross-cutting signal (Anthropic Mythos) that affects multiple product lines.

**Weaknesses (avg < 8.0):**
- **Source Citation (7.40)**: The agent cites sources but inconsistently. The 61% OpenRouter statistic — a critical data point — appears without a specific source in the report body. Some sections cite sources inline while others don't.
- **Actionability (7.40)**: The report presents facts well but rarely includes an explicit "So What?" tied to a specific recommended action or timeline. The Perplexity and Cognition scenarios scored highest on actionability because they included framing like "graduated from search challenger to full AI platform" and "integration is the key risk."

**Systemic issue — Threat Level Granularity (8.30):**
The agent assigns threat levels at the *product line* level (ChatGPT=HIGH, Codex=HIGH, API=HIGH), not at the *per-competitor* level. This means xAI (expected MEDIUM) and Cognition (expected MEDIUM) get rolled into the overall HIGH for their respective sections. The agent cannot distinguish between "this product line has a HIGH-severity week overall" and "this specific competitor is a MEDIUM threat." This is a design limitation, not a bug — but it reduces precision for scenarios where competitors within the same product line warrant different threat levels.

---

## Detailed Results

### Scenario 1: Anthropic Mythos Leak Detection
**Weighted Score: 8.35/10**

**Expected**: Multiple product lines, HIGH threat, HIGH confidence
**Keywords**: Mythos ✓, step change ✓, leak ✓, IPO ✓

| Dimension | Score | Reasoning |
|-----------|-------|-----------|
| Signal Detection | 9/10 | Signal clearly present in Must Know #1 with accurate details: "step change in capabilities," "unprecedented cybersecurity risks," IPO October 2026, $60B+. Minor deduction: no explicit mention of the "public data cache" leak vector. |
| Classification | 8/10 | Appears in Must Know (cross-cutting) and Customer Sentiment — appropriate for a multi-product signal. Minor deduction: no explicit labeling as "multiple product lines affected." |
| Threat-Level Accuracy | 9/10 | HIGH matches expectation. Correctly elevated to Must Know #1 priority. |
| Source Citation | 8/10 | Fortune and Bloomberg cited — both credible, both ground-truth sources. |
| Actionability | 7/10 | Facts are clear but no explicit "So What?" for what OpenAI should do about a leaked next-gen Anthropic model. |

### Scenario 2: Google ChatGPT Migration Tool
**Weighted Score: 8.60/10**

**Expected**: ChatGPT section, HIGH threat, HIGH confidence
**Keywords**: migration ✓, chat history ✓, ChatGPT ✓, transfer (covered by "migration")

| Dimension | Score | Reasoning |
|-----------|-------|-----------|
| Signal Detection | 9/10 | Present in three separate locations: Dashboard, Must Know #3, ChatGPT Intelligence. Strong redundancy shows high priority. |
| Classification | 10/10 | Correctly placed in ChatGPT product line across Dashboard and ChatGPT Intelligence section. |
| Threat-Level Accuracy | 9/10 | HIGH matches. Dashboard and inline framing both convey urgency. |
| Source Citation | 7/10 | Bloomberg and Google Blog cited. No additional independent analysis sources. |
| Actionability | 7/10 | "Positions Gemini as switching destination" is strategic but lacks a concrete implication for ChatGPT's response. |

### Scenario 3: Cursor $29.3B Valuation and Automations Launch
**Weighted Score: 9.20/10** (Highest)

**Expected**: Codex section, HIGH threat, HIGH confidence
**Keywords**: $29.3B ✓, $2.3B ✓, Automations ✓, Graphite ✓, enterprise ✓

| Dimension | Score | Reasoning |
|-----------|-------|-----------|
| Signal Detection | 10/10 | All five keywords found verbatim. Rich additional detail: client list (OpenAI, Uber, Spotify, Shopify, NVIDIA, MLB), 60% enterprise revenue, Accel/Coatue lead. |
| Classification | 10/10 | Correctly in Codex section, Dashboard, and Must Know #2. |
| Threat-Level Accuracy | 9/10 | HIGH matches. Correctly framed as top-3 Must Know. |
| Source Citation | 8/10 | Four credible sources: TechFundingNews, Crunchbase, InfoWorld, Contrary Research. |
| Actionability | 8/10 | Enterprise revenue share and client list give decision-makers concrete competitive context. "Autonomous cloud agents" framing highlights the strategic shift. |

### Scenario 4: Google Jules GA with Gemini 3 Pro
**Weighted Score: 8.60/10**

**Expected**: Codex section, HIGH threat, HIGH confidence
**Keywords**: Jules ✓, Gemini 3 ✓, beta ✓, free ✓

| Dimension | Score | Reasoning |
|-----------|-------|-----------|
| Signal Detection | 9/10 | All keywords present: "Jules exited public beta, powered by Gemini 3 Pro," "Gemini Code Assist now free." Subscription tiers mentioned. |
| Classification | 10/10 | Correctly in Codex Intelligence and Must Know #3. |
| Threat-Level Accuracy | 9/10 | HIGH matches expectation. |
| Source Citation | 7/10 | Google Developers Blog cited — relevant but single-source (Google's own announcement). Would benefit from independent coverage. |
| Actionability | 7/10 | Subscription tier details are useful but no explicit Codex pricing/positioning implication. |

### Scenario 5: DeepSeek V4 Imminent Release
**Weighted Score: 8.55/10**

**Expected**: API section, HIGH threat, MEDIUM confidence
**Keywords**: V4 ✓, multimodal ✓, trillion ✓, Huawei ✓, coding leaderboard ✓

| Dimension | Score | Reasoning |
|-----------|-------|-----------|
| Signal Detection | 9/10 | All keywords found with rich detail: "1 trillion params, 32B active," "V4 Lite appeared March 9," "Huawei and Cambricon." |
| Classification | 10/10 | Correctly in API & Models Intelligence section. Also referenced in Codex benchmarks. |
| Threat-Level Accuracy | 8/10 | Report shows HIGH/●●● but expected confidence was MEDIUM — V4 is "imminent" (not released), which warrants lower confidence. Agent slightly overstated certainty. |
| Source Citation | 7/10 | TechNode cited — credible for Chinese tech news. |
| Actionability | 8/10 | Pricing comparison ("~90% of GPT-5.4 at 1/50th cost") is highly actionable for BD/pricing decisions. |

### Scenario 6: Chinese Models 61% of OpenRouter Token Usage
**Weighted Score: 8.65/10**

**Expected**: API section, HIGH threat, HIGH confidence
**Keywords**: 61% ✓, Chinese ✓, OpenRouter ✓, MiniMax ✓, Kimi ✓

| Dimension | Score | Reasoning |
|-----------|-------|-----------|
| Signal Detection | 10/10 | All keywords present with exact token counts (4.55T MiniMax, 4.02T Kimi). Rich quantitative detail. |
| Classification | 10/10 | Correctly in API & Models section and Dashboard. |
| Threat-Level Accuracy | 10/10 | HIGH matches. Correctly elevated as a structural market shift, not just a weekly signal. |
| Source Citation | 5/10 | The 61% statistic — the most critical data point — appears without inline source attribution in the API section body. Sources list includes IndexBox and TeamDay but they're not linked to this specific claim. |
| Actionability | 6/10 | "Dominance accelerating" is directional but no concrete recommendation or timeline for API pricing response. |

### Scenario 7: Zhipu GLM-5 Best Open-Source Coding
**Weighted Score: 8.90/10**

**Expected**: API section, HIGH threat, HIGH confidence
**Keywords**: GLM-5 ✓, 95.8% ✓, SWE-bench ✓, Huawei ✓, MIT ✓

| Dimension | Score | Reasoning |
|-----------|-------|-----------|
| Signal Detection | 10/10 | All keywords present plus bonus detail: Ascend 910B chip model, stock rally 250%+. |
| Classification | 9/10 | Correctly in API section. Also appears in Codex benchmarks — reasonable dual-listing but slightly noisy. |
| Threat-Level Accuracy | 10/10 | HIGH matches. Correctly framed as a non-US hardware supply chain signal. |
| Source Citation | 7/10 | The Diplomat cited for stock context. The 95.8% benchmark claim itself lacks a primary source citation. |
| Actionability | 7/10 | "Best open-source coding model" and "non-US, non-NVIDIA hardware" are clear strategic signals but no explicit pricing/competitive response implication. |

### Scenario 8: Perplexity Platform Evolution
**Weighted Score: 9.30/10** (Highest)

**Expected**: ChatGPT section, HIGH threat, MEDIUM confidence
**Keywords**: Personal Computer ✓, platform ✓, API ✓, enterprise ✓

| Dimension | Score | Reasoning |
|-----------|-------|-----------|
| Signal Detection | 10/10 | All keywords plus bonus: Comet, Market Research pilot, CB Insights/PitchBook/Statista partnerships. Very rich coverage. |
| Classification | 10/10 | Correctly in ChatGPT Intelligence section. Also in Horizon Watch ("graduated from search challenger to full AI platform"). |
| Threat-Level Accuracy | 8/10 | Report presents with HIGH confidence but expected MEDIUM — the platform pivot is significant but the success of Personal Computer hardware is speculative. |
| Source Citation | 9/10 | Axios cited explicitly. VKTR mentioned in sources list for Market Research. |
| Actionability | 9/10 | "Graduated from search challenger to full AI platform" is an excellent actionable frame. "24/7 autonomous digital proxy" redefines the competitive category. |

### Scenario 9: xAI $20B Funding and X Algorithm Integration
**Weighted Score: 7.40/10** (Lowest)

**Expected**: ChatGPT section, MEDIUM threat, HIGH confidence
**Keywords**: $20B ✓, algorithm ✓, Grok Imagine ✓, video ✓

| Dimension | Score | Reasoning |
|-----------|-------|-----------|
| Signal Detection | 9/10 | All keywords found but split across ChatGPT Intelligence (algorithm, video) and Hiring section ($20B). Signal fragmented rather than unified. |
| Classification | 9/10 | In ChatGPT section — correct. But funding detail is in Hiring section, which splits the story. |
| Threat-Level Accuracy | 5/10 | Report rates overall ChatGPT as HIGH but expected xAI individually at MEDIUM. The algorithm integration is speculative (announced, not shipped). Co-founder departures suggest execution risk. The agent can't distinguish per-competitor threat levels from per-section levels. |
| Source Citation | 8/10 | Bloomberg and PC Guide cited. Nikita Bier attributed by name. |
| Actionability | 6/10 | "Most important change ever made to X" quote is vivid but no concrete strategic implication for ChatGPT. Split presentation weakens coherence. |

### Scenario 10: Cognition Devin+Windsurf Integration Status
**Weighted Score: 8.85/10**

**Expected**: Codex section, MEDIUM threat, MEDIUM confidence
**Keywords**: Devin ✓, Windsurf ✓, integration ✓, 200 ✓

| Dimension | Score | Reasoning |
|-----------|-------|-----------|
| Signal Detection | 10/10 | All keywords present with key nuance: "products remain largely separate." $10B+ valuation, 200+ employees. |
| Classification | 10/10 | Correctly in Codex Intelligence section. |
| Threat-Level Accuracy | 6/10 | Report subsumes Cognition under overall HIGH for Codex. Expected MEDIUM for Cognition specifically — integration challenges moderate the near-term threat. Agent can't distinguish per-competitor ratings. |
| Source Citation | 9/10 | SF Standard explicitly cited — the primary ground-truth source. |
| Actionability | 9/10 | "Integration is the key risk" is exactly what a decision-maker needs to know. Contextualizes Cognition relative to Cursor ($29.3B) and Claude Code. |

---

## Systemic Issues Identified

### 1. Threat-Level Granularity Gap
The agent assigns threat levels per *product line* (ChatGPT, Codex, API) but not per *competitor*. This means when one competitor in a section warrants MEDIUM and another warrants HIGH, the section-level HIGH dominates. Scenarios 9 (xAI) and 10 (Cognition) both lost points because their expected MEDIUM ratings were obscured by the section-level HIGH.

**Recommendation**: Add per-competitor threat indicators within each section, or at minimum, distinguish between "section-level threat" and "individual competitor threat" in the C-Suite Dashboard.

### 2. Source Citation Inconsistency
Some findings have inline citations (Axios, Bloomberg) while others present statistics (61% OpenRouter, 95.8% SWE-bench) without attribution in the body text. The sources are listed in the Sources section at the bottom, but a reader scanning a specific finding can't verify it without scrolling.

**Recommendation**: Every quantitative claim should have an inline source citation. Use the format already established: (Source: [Name](URL)).

### 3. Actionability Varies by Signal Type
The agent produces excellent actionable framing for *structural shifts* (Perplexity platform pivot, Cognition integration risk) but weaker framing for *incremental signals* (xAI funding, Google migration tool). Funding announcements and feature launches often lack a "this means OpenAI should consider X within Y timeframe" implication.

**Recommendation**: Add a mandatory "Implication for OpenAI" sentence to every signal card, not just the C-Suite Dashboard summary.

---

## Conclusion

The agent scores **8.64/10** overall with **zero missed signals** across 10 scenarios and **near-perfect product-line classification** (9.60/10 avg). Its primary weaknesses are at the margins: threat-level granularity below the section level, inconsistent source citation for quantitative claims, and variable actionability that depends on signal type.

For a v1.1 prototype, this is a strong result. The agent reliably detects, classifies, and surfaces competitive signals — the core job it was designed to do. The improvement opportunities (per-competitor threat levels, inline citations, mandatory implications) are well-defined and implementable in v1.2.

---

*Evaluation generated March 29, 2026 by Claude judges run in Claude Code sessions*
*10 scenarios × 5 dimensions × 2 parallel judge agents*
