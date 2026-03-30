# Industry Benchmarks & Market Data

> Reference data for the agent to provide quantitative context when evaluating competitive signals. Update monthly or when major benchmarks are published.

## Model Performance — Chatbot Arena (LMSYS, as of March 2026)

| Rank | Model | Provider | Elo (approx) | Open/Closed |
|------|-------|----------|-------------|-------------|
| 1 | Claude Opus 4.6 | Anthropic | ~1504 | Closed |
| 2 | Gemini 3.1 Pro Preview | Google DeepMind | ~1500 | Closed |
| 3 | GPT-5.2 | OpenAI | ~1500 | Closed |
| 4 | Grok 4.20 Beta1 | xAI | ~1493 | Closed |
| 5 | Gemini 3 Pro | Google DeepMind | ~1485 | Closed |
| 6 | ByteDance Seed 2.0 | ByteDance | -- | Closed |
| 8 | Gemini 3 Flash | Google DeepMind | ~1473 | Closed |

*Note: Claude Opus 4.6 and GPT-5.2 are in a statistical dead heat for #1. Grok 4.20 leads the agentic index (68.7). Gemini 3.1 Pro is #1 on 12 of 18 tracked benchmarks.*

## Coding Benchmarks (HumanEval / SWE-Bench Verified)

| Model | Provider | SWE-Bench Verified | Open/Closed | Notes |
|-------|----------|-------------------|-------------|-------|
| GLM-5 | Zhipu AI | ~95.8% | Open (MIT) | Best open-source coding, trained on Huawei Ascend 910B |
| Kimi K2.5 | Moonshot AI | ~76.8% | Open (MIT) | Strong for open-weight, natively multimodal |
| Claude Sonnet 4.6 | Anthropic | ~55% | Closed | Leading closed-source on real-world coding |
| GPT-4o | OpenAI | ~51% | Closed | Solid but trailing Claude on SWE-Bench |
| Gemini 3.1 Pro | Google | ~49% | Closed | Improving rapidly |
| DeepSeek V4 | DeepSeek | ~45% | Open | Impressive for cost tier |

*Note: SWE-Bench Verified measures real-world bug fixing on GitHub issues. GLM-5's 95.8% is a standout result for open-source.*

## Reasoning Benchmarks (GPQA / MATH-500)

| Model | Provider | GPQA Diamond | MATH-500 | Notes |
|-------|----------|-------------|----------|-------|
| o3 | OpenAI | ~68% | ~97% | Reasoning specialist |
| Claude Opus 4.6 | Anthropic | ~65% | ~96% | Close competitor |
| Gemini 3.1 Pro | Google | ~63% | ~95% | Closing gap |
| DeepSeek V4-Speciale | DeepSeek | ~80% | ~95% | Surpasses GPT-5 on some reasoning benchmarks |
| DeepSeek R1 | DeepSeek | ~60% | ~94% | Strong for cost tier |

## General Reasoning (MMLU / MMLU-Pro)

| Model | Provider | MMLU | Open/Closed |
|-------|----------|------|-------------|
| DeepSeek V4 | DeepSeek | ~94.2% | Open |
| Claude Opus 4.6 | Anthropic | ~89% | Closed |
| GPT-4o | OpenAI | ~88% | Closed |
| Gemini 3.1 Pro | Google | ~88% | Closed |
| Qwen 3.5 | Alibaba | ~87% | Open |
| Grok 4.20 | xAI | ~87% | Closed |
| LLaMA 4 Maverick | Meta | ~86% | Open |

## API Pricing Comparison (per million tokens, as of March 2026)

### Closed-Source APIs

| Provider | Model | Input | Output | Context Window |
|----------|-------|-------|--------|----------------|
| OpenAI | GPT-5.4 | TBD | TBD | 1M (unified Codex + GPT, built-in computer use) |
| OpenAI | GPT-4o | $2.50 | $10.00 | 128K |
| OpenAI | GPT-4o mini | $0.15 | $0.60 | 128K |
| Anthropic | Claude Opus 4.6 | $15.00 | $75.00 | 1M |
| Anthropic | Claude Sonnet 4.6 | $3.00 | $15.00 | 200K |
| Anthropic | Claude Haiku 4.5 | $0.80 | $4.00 | 200K |
| Google | Gemini 3.1 Pro | $1.25 | $5.00 | 1M |
| Google | Gemini 3 Flash | $0.15 | $0.60 | 1M |
| xAI | Grok 4.20 | TBD | TBD | 2M |
| Mistral | Large 3 | $2.00 | $6.00 | 256K |

### Open-Source/Open-Weight (Self-host or via OpenRouter)

| Provider | Model | Input | Output | Context | License |
|----------|-------|-------|--------|---------|---------|
| DeepSeek | V4 | ~$0.25 | ~$0.38 | 1M+ | Open |
| Alibaba | Qwen 3.5 | varies | varies | 262K | Open |
| Zhipu AI | GLM-5 | varies | varies | 128K | MIT |
| Moonshot | Kimi K2.5 | varies | varies | 200K+ | MIT |
| MiniMax | M2.5 | varies | varies | 128K | Open |
| Meta | LLaMA 4 Maverick | free | free | 1M | Open |
| Meta | LLaMA 4 Scout | free | free | 10M | Open |
| NVIDIA | Nemotron 3 Super | free | free | 262K | Open |

*Pricing changes frequently. Open-source pricing depends on hosting provider. Verify before citing in reports.*

## Market Context

### Consumer AI Chat Market
- ChatGPT estimated at ~300M+ monthly active users (largest)
- Claude growing rapidly, especially among power users and developers
- Gemini has distribution advantage via Google products but lower engagement
- Perplexity growing fast in search-as-chat niche
- Grok limited to X/Twitter premium subscribers
- Kimi and Doubao dominating Chinese consumer market

### Enterprise AI Coding Market
- Key players: GitHub Copilot (incumbent), Cursor (disruptor), Claude Code, Gemini Code Assist, Cognition (Devin + Windsurf)
- Cursor has strongest developer momentum; Copilot has largest installed base
- Google's free tier for teams <25 is the most aggressive pricing move this quarter
- Devin represents the "autonomous agent" future — different paradigm from copilot tools

### API & Developer Platform Market
- Estimated $50B+ market by 2027
- **Chinese models now 61% of OpenRouter token consumption** (up dramatically)
- Programming is 50%+ of all API tokens (up from 11% in early 2025)
- Agent-driven workflows generate more than half of all output tokens
- Open-weight models closing gap with proprietary on benchmarks
- Free tier models (Nemotron, GPT-OSS, Qwen3-Coder) driving experimentation

### Open-Source Ecosystem
- Hugging Face: 1.5M+ models hosted
- LLaMA downloads: 1B+ cumulative
- Key open-source leaders: DeepSeek, Qwen, Zhipu/GLM, Moonshot/Kimi, Meta/LLaMA
- Trend: MIT-licensed frontier models (GLM-5, Kimi K2.5) lowering barrier to self-hosting

---

*Last updated: March 29, 2026 (Jack's review — updated with LMSYS Arena, HuggingFace, and OpenRouter data)*
