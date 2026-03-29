const express = require("express");
const cors = require("cors");
const Anthropic = require("@anthropic-ai/sdk").default;
const path = require("path");

const app = express();
app.use(cors());
app.use(express.json({ limit: "1mb" }));

// Serve the setup wizard as the homepage
app.use(express.static(path.join(__dirname, "../setup-wizard")));

// Health check
app.get("/api/health", (req, res) => {
  res.json({ status: "ok" });
});

// Generate report using the user's API key
app.post("/api/generate", async (req, res) => {
  const { apiKey, config } = req.body;

  if (!apiKey || !apiKey.startsWith("sk-ant-")) {
    return res.status(400).json({ error: "Invalid API key format. Must start with sk-ant-" });
  }
  if (!config || !config.company) {
    return res.status(400).json({ error: "Missing company config" });
  }

  // Build the prompt from user's config
  const prompt = buildPrompt(config);

  // Create a client with the USER's key — we never store it
  const client = new Anthropic({ apiKey });

  try {
    const message = await client.messages.create({
      model: "claude-sonnet-4-6",
      max_tokens: 12000,
      messages: [{ role: "user", content: prompt }],
    });

    const reportContent = message.content[0].text;
    res.json({ report: reportContent, usage: message.usage });
  } catch (err) {
    if (err.status === 401) {
      return res.status(401).json({ error: "Invalid API key. Check your key and try again." });
    }
    if (err.status === 429) {
      return res.status(429).json({ error: "Rate limited. Wait a minute and try again." });
    }
    console.error("Claude API error:", err.message);
    res.status(500).json({ error: "Failed to generate report. " + err.message });
  }
});

function buildPrompt(config) {
  const { company, products, tier1, tier2, channels, subreddits } = config;

  const productLines = products
    .map((p) => `- **${p.name}** (${p.type}) — Stakeholder: ${p.stakeholder}`)
    .join("\n");

  const tier1List = tier1.map((c) => `- ${c}`).join("\n");
  const tier2List = tier2.length ? tier2.map((c) => `- ${c}`).join("\n") : "- (none specified)";
  const channelList = channels.map((c) => `- ${c}`).join("\n");
  const subList = subreddits.length ? subreddits.map((s) => `- ${s}`).join("\n") : "- (none specified)";

  return `You are a Competitive Intelligence Analyst. Generate a structured competitive intelligence report.

## Your Company
**${company.name}** — ${company.description || ""}

### Product Lines
${productLines}

## Competitors to Monitor

### Tier 1 — Core Competitors (deep analysis)
${tier1List}

### Tier 2 — Rising Challengers (scan for notable signals)
${tier2List}

## Search Scope
Analyze the latest publicly available information across these channels:
${channelList}

${subreddits.length ? `### Reddit Subreddits\n${subList}` : ""}

## Report Format

Structure the report EXACTLY as follows. Use markdown formatting.

### 1. C-Suite Dashboard
Create a threat-level table:
| Product Line | Threat Level | Confidence | So What? |
For each product line, rate: HIGH / MEDIUM / LOW with confidence dots.

### 2. Must Know This Week
List the top 3 most strategically significant signals. Format each as:
**Company Name** — One-line signal description

### 3. Product Line Sections
For EACH product line, create a section with findings. Each finding must be:
- Formatted as: **Company Name** — Signal headline
- Followed by exactly 1-2 bullet points (no paragraphs)
- Include source citations where possible

### 4. Hiring & Resource Signals
Notable hiring patterns, funding rounds, or resource moves from competitors.

### 5. Horizon Watch
Tier 2 challengers and emerging tech worth monitoring.

## Critical Rules
- Every finding starts with **Company Name** —
- Max 2 bullet points per finding. No paragraphs.
- Be specific. Cite sources when available.
- If you cannot find signals for a section, say so. Do not fabricate.
- Distinguish confirmed facts from speculation.
- Prioritize signal over noise — an exec should get value in 5 minutes.`;
}

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
