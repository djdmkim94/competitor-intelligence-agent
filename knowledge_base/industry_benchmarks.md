# Industry Benchmarks & Market Data

> Reference data for the agent to provide quantitative context when evaluating competitive signals. Update monthly or when major benchmarks are published.

## Model Performance Leaderboards (as of March 2026)

### General Reasoning (MMLU / MMLU-Pro)
| Model | MMLU | MMLU-Pro | Notes |
|-------|------|----------|-------|
| GPT-4o | ~88% | ~73% | OpenAI's current flagship |
| Claude Opus 4.6 | ~89% | ~74% | Anthropic's latest |
| Gemini 2.5 Pro | ~88% | ~73% | Google's latest |
| Grok 3 | ~87% | ~71% | xAI |
| LLaMA 4 Maverick | ~86% | ~70% | Meta's open-weight |
| DeepSeek V3 | ~85% | ~69% | Significant for the cost |

*Note: Benchmark numbers are approximate and self-reported. Cross-model comparisons should be treated with caution.*

### Coding (HumanEval / SWE-Bench Verified)
| Model | HumanEval | SWE-Bench Verified | Notes |
|-------|-----------|-------------------|-------|
| Claude Sonnet 4.6 | ~93% | ~55% | Strong real-world coding |
| GPT-4o | ~92% | ~51% | Solid but trailing on SWE-Bench |
| Gemini 2.5 Pro | ~91% | ~49% | Improving rapidly |
| DeepSeek V3 | ~89% | ~45% | Impressive for cost tier |

### Reasoning (GPQA / MATH-500)
| Model | GPQA Diamond | MATH-500 | Notes |
|-------|-------------|----------|-------|
| o3 (OpenAI) | ~68% | ~97% | Reasoning specialist |
| Claude Opus 4.6 | ~65% | ~96% | Close competitor |
| Gemini 2.5 Pro | ~63% | ~95% | Closing gap |
| DeepSeek R1 | ~60% | ~94% | Remarkable for cost |

## API Pricing Comparison (per million tokens, as of March 2026)

| Provider | Model | Input | Output | Context Window |
|----------|-------|-------|--------|----------------|
| OpenAI | GPT-4o | $2.50 | $10.00 | 128K |
| OpenAI | GPT-4o mini | $0.15 | $0.60 | 128K |
| Anthropic | Claude Sonnet 4.6 | $3.00 | $15.00 | 200K |
| Anthropic | Claude Haiku 4.5 | $0.80 | $4.00 | 200K |
| Google | Gemini 2.5 Pro | $1.25 | $5.00 | 1M |
| Google | Gemini 2.5 Flash | $0.15 | $0.60 | 1M |
| DeepSeek | V3 | $0.27 | $1.10 | 128K |
| Mistral | Large | $2.00 | $6.00 | 128K |

*Pricing changes frequently. Verify before citing in reports.*

## Market Context

### Consumer AI Chat Market
- ChatGPT estimated at ~300M+ monthly active users (largest)
- Claude growing rapidly, especially among power users and developers
- Gemini has distribution advantage via Google products but lower engagement
- Grok limited to X/Twitter premium subscribers

### Enterprise AI Market
- Estimated $50B+ market by 2027
- Key battleground: coding assistants, enterprise search/RAG, workflow automation
- Buyers care most about: data privacy, compliance, integration, reliability
- AWS Bedrock + Claude partnership is a significant distribution channel for Anthropic

### Open-Source Ecosystem
- Hugging Face: 1.5M+ models hosted
- LLaMA downloads: 1B+ cumulative
- Trend: open-weight models closing gap with proprietary on benchmarks, but enterprise support/reliability still favors proprietary

---

*Last updated: March 28, 2026*
