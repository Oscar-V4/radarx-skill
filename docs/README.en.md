# RadarX

<p align="center">
  <a href="../README.md">한국어</a> |
  <b>English</b> |
  <a href="README.zh-CN.md">简体中文</a>
</p>

**RadarX is a radar-style research skill for finding fresh AI, open-source, social, and community signals.**  
It scans live sources such as Threads, X, Reddit, Hacker News, GitHub, YouTube, Hugging Face, arXiv, Product Hunt, and the web, then uses a public access ladder and provenance labels to separate validated recommendations from weak but useful trend signals.

- Finds recent AI tools, open-source projects, agentic workflows, best practices, and project-idea signals.
- Connects to a local Threads archive when available, while keeping archive context separate from live evidence.
- Uses GitHub, official docs, Reddit/HN, YouTube, arXiv, Hugging Face, Product Hunt, and web search in source layers.
- Tries reader-proxy, public APIs, RSS/feed, metadata, cache/archive, and optional browser sessions when normal browsing fails.
- Scores candidates by relevance, evidence, freshness, novelty, adoption, and safety.
- Separates social-only, reader-proxy-only, metadata-only, cache/archive, and login-required leads from strong recommendations.
- Applies access-quality caps so weakly accessed material is not over-promoted.
- Expands project-idea research into baselines, MVP paths, evaluation plans, and risk gates.

## Quick Install

Share this prompt with a friend. They can paste it into Codex, Claude Code, Antigravity, or another coding agent and let the agent install the skill.

```text
Please inspect this GitHub repo and install the RadarX agent skill:
https://github.com/Oscar-V4/radarx-skill

Detect the agent environment you are running in.
- If this is Codex, install it into ~/.codex/skills/radarx.
- If this is Claude Code, install it into ~/.claude/skills/radarx.
- If this is another agent, check whether it supports SKILL.md-based skill folders and install it in the closest user-level skill location.
- Use a built-in skill installer if available; otherwise clone the repo and copy skills/radarx into the user skill directory.

After installation, read skills/radarx/SKILL.md and README.md, then explain:
1. when I should use $radarx
2. how I should phrase requests
3. three starter prompts to test it
```

Direct Codex install:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo Oscar-V4/radarx-skill \
  --path skills/radarx
```

Restart your agent app after installation, then invoke the skill with `$radarx`.

## When To Use It

| Situation | Say this |
|---|---|
| You want recent AI/open-source signals | `$radarx Find recent open-source tools for real-time AI voice agents.` |
| You want to validate social hype | `$radarx Check whether this tool trending on X/Threads is actually useful, with evidence.` |
| You are researching a contest or hackathon idea | `$radarx Research the information, baselines, and MVP path for this AI contest idea.` |
| You want archive-aware discovery | `$radarx Connect this to my Threads archive and find similar but newer AI workflow examples.` |
| You do not want a link dump | `$radarx Give me at most three strong candidates and explain rejected weak signals.` |
| Live social coverage matters | `$radarx Use social-heavy mode across X, Threads, Reddit, and Hacker News first.` |

## Output Shape

RadarX usually returns:

- **Intent**: the problem and what counts as a useful candidate
- **Attention Mode**: quick, balanced, deep, social-heavy, or archive-first
- **Archive Connections**: related saved/archive context
- **Access Coverage**: available archive, public web, reader-proxy, public API, browser session, or paid API coverage
- **Strong Finds**: source-backed candidates and URLs
- **Trending Signals**: fresh high-fit signals that are still weakly verified
- **Access-Limited Leads**: partial, reader-proxy-only, metadata-only, cache/archive, or login-required leads
- **Rejected Or Weak Signals**: what was ignored and why
- **Next Searches**: queries, communities, docs, or authors to explore next

For project ideas and MVP planning, it expands into baseline reality, build paths, evaluation plans, and privacy/safety risk gates.

## Compatibility

This repo is packaged as a `SKILL.md`-based agent skill. Agents such as Codex and Claude Code can install it as a user skill. Other agents can still use it by reading `skills/radarx/SKILL.md`, though automatic skill discovery rules vary by product.

## Requirements

RadarX does not require X/Threads login, Playwright, browser-use, Chrome automation, or paid scraping APIs for normal use. It uses public evidence first and treats logged-in, paid, or browser-dependent sources as optional enhanced adapters.

When browser plugins or logged-in sessions are available, RadarX can inspect more live/social material, but results should still carry `access_method`, `access_quality`, and `provenance_note` labels.

Do not export cookies or tokens just to use RadarX. If a source is unavailable, the skill should state the limitation and continue with public fallback evidence.
