---
name: radarx
description: Discover recent AI, open-source, agentic workflow, MCP, coding-agent, best-practice, project-idea, and use-case research signals across live social/community sources and reliable public sources. Use when the user asks to find fresh examples, tools, workflows, posts, community signals, emerging practices, or the information needed to build/evaluate an AI or open-source idea from Threads, X, Reddit, Hacker News, GitHub, YouTube, Bluesky, Mastodon, Product Hunt, Hugging Face, arXiv, official docs, or the web; especially when results must be archive-aware, evidence-gated, and aggressively filtered for weak social noise.
---

# RadarX

Use this skill to find useful live candidates, not to maximize recall. It should discover fresh AI/tool/workflow/project signals, connect them to the user's existing Threads archive when available, and reject weak or noisy social results.

This skill is separate from `threads-archive`: the archive is the trusted personal knowledge base; live social results are volatile candidates until verified.

## Requirements

RadarX has no hard dependency on X/Threads login, Playwright, browser-use, Chrome automation, paid scraping APIs, or official social APIs.

Use available low-friction sources first: local archive snapshots, GitHub, official docs, Reddit, Hacker News, YouTube transcripts, arXiv, Hugging Face, Product Hunt, and web search. Treat browser automation, logged-in X/Threads sessions, official APIs, and paid social search services as optional adapters.

If X/Threads login or browser automation is unavailable, use public fallback searches such as `site:x.com` or `site:threads.com`, then state the limitation in the report. Do not ask users to export cookies or tokens just to run this skill.

## Core Rule

Maximize useful, archive-aware, evidence-backed discovery by aggressively rejecting weak live social signals.

Never let X/Threads virality override weak relevance or weak evidence. Treat "no strong live candidates found" as a successful outcome.

## Workflow

1. Define the intent contract.
   - Classify the request: tool discovery, use-case discovery, project-idea research, best-practice scan, workflow comparison, trend pulse, person/company brief, or "archive gap" search.
   - State what would count as a useful candidate and what should be rejected.
   - If the request is broad, narrow it to AI/open-source/agentic-workflow usefulness rather than general news.
   - For "I want to build..." or "what information do I need..." requests, load `references/research-brief-playbook.md`.

2. Anchor on the user's archive when available.
   - If `threads-archive` is installed or the synced vault exists, search it first for related topics, keywords, authors, and already-known candidates.
   - Use the archive to detect duplicates, infer taste, and generate query variants.
   - Do not treat archive matches as live evidence; label them as "Archive Connections".

3. Choose an attention mode.
   - Default to `balanced`.
   - Use `quick` when the user wants a lightweight scan.
   - Use `deep` when recommendations will drive meaningful time or money.
   - Use `deep` for human-impact domains such as accessibility, health, education, minors, safety, legal, privacy, or financial decisions.
   - Use `social-heavy` only when the user explicitly asks for X/Threads/social-first discovery.
   - Use `archive-first` when the user asks for "more like what I saved".
   - Load `references/attention-policy.md` for budgets, scoring, and gates.

4. Scout sources in layers.
   - Reliable public layer: GitHub, official docs, Reddit, Hacker News, YouTube transcripts, reputable web search.
   - For product or project ideas, identify incumbent baselines before recommending a build path.
   - Optional live social layer: X, Threads, Bluesky, Mastodon, Product Hunt, TikTok/Instagram only when available and appropriate.
   - Paid or credentialed sources must stay optional and best-effort unless the user explicitly requests setup.
   - Load `references/source-playbook.md` for source-specific tactics and fallback order.

5. Score candidates before synthesizing.
   - Use the Evidence Ladder and Candidate Judge in `references/attention-policy.md`.
   - For larger result sets, write a temporary JSON candidate list outside project repos and run `scripts/score_candidates.py`.
   - Only A/B candidates belong in the main answer.

6. Run the skeptic pass.
   - Ask whether each strong candidate is just promotion, SEO, a single viral post, stale, already in the archive, unsupported by code/docs, or unrelated to the user's actual problem.
   - Downgrade or reject anything that fails.

7. Report using the output contract.
   - Separate `Strong Finds`, `Volatile Social Signals`, `Archive Connections`, `Rejected/Weak Signals`, and `Next Searches`.
   - For project-idea research, use the research brief form in `references/output-contract.md`.
   - Cite URLs for every candidate.
   - Load `references/output-contract.md` for the report shape.

## Source Priority

Default order:

1. Threads archive, when present
2. GitHub repos, releases, issues, discussions, stars velocity
3. Reddit communities and comments
4. Hacker News stories/comments
5. YouTube transcripts and demo videos
6. Official docs, changelogs, product pages
7. X and Threads live/search adapters
8. Bluesky, Mastodon, Product Hunt, Hugging Face, arXiv, Papers with Code, web search

X and Threads are important but volatile. Use them as candidate discovery sources, not as standalone proof.

## Permission Boundaries

Allowed by default:

- Search public web/GitHub/docs.
- Read local synced archive snapshots.
- Use currently available browser/search tools in a best-effort way.
- Continue with public fallback sources when browser automation or logged-in social sessions are unavailable.
- Inspect public GitHub metadata and the user's stars when authenticated.
- Produce candidate reports and recommended next searches.

Do not do these unless the user explicitly asks:

- Install packages, skills, MCP servers, browser extensions, or CLIs.
- Create accounts, start trials, or subscribe to paid APIs.
- Store API keys or browser cookies.
- Export or inspect social-media cookies/session stores.
- Add live-source results into the Threads archive automatically.
- Run recurring monitors or schedulers.
- Modify project files for the user.

## Good Outputs

Good outputs are small, ranked, skeptical, and source-backed. Prefer three strong candidates over twenty weak links. When live social evidence is thin, say so directly and recommend better query/source angles.

## Resources

- `references/attention-policy.md`: attention modes, evidence ladder, scoring rubric, social caps, rejection rules.
- `references/source-playbook.md`: source adapters, query tactics, fallback order, and setup friction.
- `references/output-contract.md`: answer format and candidate fields.
- `references/research-brief-playbook.md`: project-idea and "needed information" research workflow, baselines, evaluation, and human-impact gates.
- `scripts/score_candidates.py`: deterministic candidate scoring helper for larger scans.
