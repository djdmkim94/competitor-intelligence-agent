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
    const htmlReport = buildHtmlReport(reportContent, config.company.name);
    res.json({ report: reportContent, html: htmlReport, usage: message.usage });
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

function buildHtmlReport(markdown, companyName) {
  const date = new Date().toLocaleDateString("en-US", { year: "numeric", month: "long", day: "numeric" });

  // Parse markdown into sections
  const lines = markdown.split("\n");
  let sections = [];
  let current = { title: "", content: [] };

  for (const line of lines) {
    if (line.startsWith("### ") || line.startsWith("## ")) {
      if (current.title || current.content.length) sections.push({ ...current });
      current = { title: line.replace(/^#+\s*/, "").replace(/^\d+\.\s*/, ""), content: [] };
    } else {
      current.content.push(line);
    }
  }
  if (current.title || current.content.length) sections.push(current);

  // Convert markdown content to HTML
  function md(text) {
    return text
      .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
      .replace(/\[(.+?)\]\((.+?)\)/g, '<a href="$2" target="_blank" style="color: #DD6B20; text-decoration: none;">$1</a>')
      .replace(/`(.+?)`/g, '<code style="background: #EDF2F7; padding: 1px 5px; border-radius: 3px; font-size: 12px;">$1</code>');
  }

  function sectionToHtml(sec) {
    let html = "";
    const lines = sec.content.filter((l) => l.trim());

    // Check for table
    const tableLines = lines.filter((l) => l.trim().startsWith("|"));
    if (tableLines.length >= 2) {
      const rows = tableLines.filter((l) => !l.includes("---"));
      html += '<div style="overflow-x: auto; margin-bottom: 16px;"><table style="width: 100%; border-collapse: collapse; font-size: 13px;">';
      rows.forEach((row, i) => {
        const cells = row.split("|").filter((c) => c.trim());
        const tag = i === 0 ? "th" : "td";
        const style =
          i === 0
            ? 'style="text-align: left; padding: 10px 12px; font-weight: 600; font-size: 12px; text-transform: uppercase; letter-spacing: 0.5px; color: #A0AEC0; border-bottom: 2px solid #E2E8F0;"'
            : 'style="padding: 10px 12px; border-bottom: 1px solid #EDF2F7; color: #718096;"';
        html += "<tr>" + cells.map((c) => `<${tag} ${style}>${md(c.trim())}</${tag}>`).join("") + "</tr>";
      });
      html += "</table></div>";
    }

    // Non-table lines
    const nonTable = lines.filter((l) => !l.trim().startsWith("|"));
    let inList = false;
    for (const line of nonTable) {
      const trimmed = line.trim();
      if (trimmed.startsWith("- ") || trimmed.startsWith("* ")) {
        if (!inList) { html += '<ul style="font-size: 13px; color: #718096; line-height: 1.7; margin: 0 0 8px 18px; padding: 0;">'; inList = true; }
        html += `<li style="margin-bottom: 4px;">${md(trimmed.slice(2))}</li>`;
      } else {
        if (inList) { html += "</ul>"; inList = false; }
        if (trimmed.startsWith("**") && trimmed.includes("—")) {
          html += `<div style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; padding: 16px 20px; margin-bottom: 10px; transition: border-color 0.2s;"><h4 style="font-size: 14px; font-weight: 600; line-height: 1.4; margin-bottom: 6px;">${md(trimmed)}</h4>`;
          // Look ahead for bullets
          const idx = nonTable.indexOf(line);
          let bullets = [];
          for (let j = idx + 1; j < nonTable.length; j++) {
            const next = nonTable[j].trim();
            if (next.startsWith("- ") || next.startsWith("* ")) bullets.push(next.slice(2));
            else break;
          }
          if (bullets.length) {
            html += '<ul style="font-size: 13px; color: #718096; line-height: 1.6; margin: 0 0 0 18px; padding: 0;">';
            bullets.forEach((b) => { html += `<li style="margin-bottom: 4px;">${md(b)}</li>`; });
            html += "</ul>";
          }
          html += "</div>";
        } else if (trimmed && !trimmed.startsWith("- ") && !trimmed.startsWith("* ")) {
          // Skip lines already consumed as bullets above
          const prevIdx = nonTable.indexOf(line);
          if (prevIdx > 0) {
            const prev = nonTable[prevIdx - 1].trim();
            if (prev.startsWith("**") && prev.includes("—")) continue;
          }
          html += `<p style="font-size: 13px; color: #718096; line-height: 1.6; margin-bottom: 8px;">${md(trimmed)}</p>`;
        }
      }
    }
    if (inList) html += "</ul>";
    return html;
  }

  // Map sections to tab content
  const dashboardSec = sections.find((s) => s.title.toLowerCase().includes("dashboard")) || { content: [] };
  const mustKnowSec = sections.find((s) => s.title.toLowerCase().includes("must know")) || { content: [] };
  const productSections = sections.filter((s) => !["dashboard", "must know", "hiring", "horizon", "source"].some((k) => s.title.toLowerCase().includes(k)) && s.title);
  const hiringSec = sections.find((s) => s.title.toLowerCase().includes("hiring")) || { content: [] };
  const horizonSec = sections.find((s) => s.title.toLowerCase().includes("horizon")) || { content: [] };

  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Sprout Scout Report — ${companyName}</title>
<link href="https://fonts.googleapis.com/css2?family=Lexend:wght@300;400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
:root {
  --bg: #FFFDF7; --surface: #FFFFFF; --surface-alt: #F7FAFC;
  --text: #2D3748; --text-secondary: #718096; --text-tertiary: #A0AEC0;
  --border: #E2E8F0; --border-light: #EDF2F7;
  --accent: #1A365D; --teal: #319795; --orange: #DD6B20;
}
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Lexend', sans-serif; background: var(--bg); color: var(--text); line-height: 1.6; -webkit-font-smoothing: antialiased; }
.container { max-width: 1080px; margin: 0 auto; padding: 48px 32px; }
.report-header { margin-bottom: 40px; padding-bottom: 24px; border-bottom: 1px solid var(--border); }
.report-header .eyebrow { font-size: 11px; font-weight: 600; letter-spacing: 1.5px; text-transform: uppercase; color: var(--teal); margin-bottom: 6px; }
.report-header h1 { font-size: 32px; font-weight: 700; color: var(--accent); letter-spacing: -0.5px; margin-bottom: 4px; }
.report-header .meta { font-size: 13px; color: var(--text-tertiary); }
.section { margin-bottom: 32px; }
.section h2 { font-size: 18px; font-weight: 700; color: var(--accent); margin-bottom: 4px; }
.section h3 { font-size: 15px; font-weight: 600; color: var(--text); margin-bottom: 4px; margin-top: 20px; }
.section .desc { font-size: 12px; color: var(--text-tertiary); margin-bottom: 16px; }
.tabs { display: flex; gap: 4px; margin-bottom: 24px; background: var(--surface-alt); padding: 4px; border-radius: 10px; border: 1px solid var(--border); }
.tab { flex: 1; padding: 9px 14px; border-radius: 7px; font-size: 13px; font-weight: 500; text-align: center; cursor: pointer; color: var(--text-secondary); border: none; background: transparent; font-family: 'Lexend', sans-serif; transition: all 0.2s; }
.tab:hover { color: var(--text); background: rgba(0,0,0,0.03); }
.tab.active { background: var(--surface); color: var(--text); box-shadow: 0 1px 3px rgba(0,0,0,0.08); }
.tab-content { display: none; }
.tab-content.active { display: block; }
.footer { margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--border); font-size: 11px; color: var(--text-tertiary); }
@media (max-width: 768px) { .container { padding: 24px 16px; } .tabs { flex-direction: column; } }
</style>
</head>
<body>
<div class="container">
  <div class="report-header">
    <div class="eyebrow">Sprout Scout</div>
    <h1>${companyName} — Intelligence Report</h1>
    <div class="meta">Generated ${date}</div>
  </div>

  <div class="section">
    <h2>C-Suite Dashboard</h2>
    <div class="desc">Threat levels, confidence scores, and key implications</div>
    ${sectionToHtml(dashboardSec)}
  </div>

  <div class="section">
    <h2>Must Know This Week</h2>
    <div class="desc">Top 3 strategically significant signals</div>
    ${sectionToHtml(mustKnowSec)}
  </div>

  <div class="tabs">
    ${productSections.map((s, i) => `<button class="tab${i === 0 ? " active" : ""}" onclick="showTab(${i})">${s.title}</button>`).join("")}
    <button class="tab" onclick="showTab(${productSections.length})">Hiring</button>
    <button class="tab" onclick="showTab(${productSections.length + 1})">Horizon</button>
  </div>

  ${productSections.map((s, i) => `<div class="tab-content${i === 0 ? " active" : ""}" id="tab-${i}"><div class="section"><h2>${s.title}</h2>${sectionToHtml(s)}</div></div>`).join("")}
  <div class="tab-content" id="tab-${productSections.length}"><div class="section"><h2>Hiring &amp; Resource Signals</h2>${sectionToHtml(hiringSec)}</div></div>
  <div class="tab-content" id="tab-${productSections.length + 1}"><div class="section"><h2>Horizon Watch</h2>${sectionToHtml(horizonSec)}</div></div>

  <div class="footer">
    Generated by Sprout Scout (Competitor Intelligence Agent). All signals sourced from publicly available information.<br>
    <a href="https://github.com/djdmkim94/competitor-intelligence-agent" style="color: var(--teal); text-decoration: none;">github.com/djdmkim94/competitor-intelligence-agent</a>
  </div>
</div>
<script>
function showTab(i) {
  document.querySelectorAll('.tab-content').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
  document.getElementById('tab-' + i).classList.add('active');
  event.target.classList.add('active');
}
</script>
</body>
</html>`;
}

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
