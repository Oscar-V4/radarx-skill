# Attention Policy

Use this reference when deciding how much attention to allocate to archive grounding, live sources, and verification.

## Modes

| Mode | Archive | Public Sources | X/Threads/Social | Verification | Synthesis | Use |
|---|---:|---:|---:|---:|---:|---|
| quick | 15 | 40 | 20 | 15 | 10 | Lightweight scan, 3-5 candidates |
| balanced | 25 | 30 | 20 | 15 | 10 | Default |
| deep | 20 | 30 | 15 | 25 | 10 | Higher confidence or spend/time decisions |
| social-heavy | 15 | 20 | 40 | 15 | 10 | User explicitly asks for X/Threads/social |
| archive-first | 40 | 25 | 15 | 10 | 10 | "More like what I saved" |

Percentages are attention budgets, not token quotas. Do not let volatile social sources consume more than their budget unless the user explicitly asks.

## Attention Triggers

Use `deep` when the request involves:

- Meaningful spend, implementation time, or tool adoption.
- Accessibility, disability, health, education, minors, safety, privacy, legal, or financial impact.
- Audio, video, biometrics, student records, health data, or other sensitive data.
- A product idea where baseline products and evaluation criteria materially affect the recommendation.

For project-idea research, spend early attention on baselines and evaluation before hunting for fresh social examples.

## Evidence Ladder

1. Official repository, documentation, release notes, source code, reproducible demo
2. High-signal community discussion with practical usage, objections, and vote/comment context
3. X/Threads/Bluesky/Mastodon posts with author identity, timestamp, and URL
4. Product pages, newsletters, blogs, SEO articles, launch posts
5. Screenshots, reposted summaries, uncited claims, scraped snippets without provenance

X/Threads can reveal fresh candidates, but they start at tier 3. Promote them only when independent evidence exists.

## Access Quality

Access quality is separate from source credibility. A high-quality source reached through a weak access path still needs provenance labels.

Use these labels while scouting:

- `full-original`: original page/API/docs/repo directly available.
- `full-public-api`: structured public endpoint, such as Reddit JSON, HN API, GitHub, arXiv, Bluesky, Mastodon, npm, PyPI, or YouTube metadata/transcript.
- `full-reader-proxy`: reader proxy such as `r.jina.ai` returned substantial text.
- `full-browser-session`: logged-in or enhanced browser session returned substantial text.
- `partial-metadata`: only OGP, JSON-LD, title, snippet, or other partial metadata.
- `cache-archive`: AMP cache, archive.today, Wayback, or another cache copy.
- `login-required`: relevant candidate identified but content requires auth, paywall, private state, or unavailable session.
- `failed`: no usable content.

Upgrade path:

- `full-original` and `full-public-api` can support `Strong Finds` when source quality is high.
- `full-reader-proxy` and `full-browser-session` can support `Strong Finds` only with independent corroboration.
- `partial-metadata`, `cache-archive`, and `login-required` usually belong in `Access-Limited Leads` or `Trending Signals`.
- `failed` belongs in `Rejected Or Weak Signals` unless the failed access itself is useful to report.

## Trending Signals

Every report should include a short `Trending Signals` section. This is not a new mode; it is a small default catchment for fresh, high-fit items that are too early or weakly verified for `Strong Finds`.

Rules:

- Include 0-3 items.
- Prefer direct fit to the user's request over broad virality.
- Use plain labels such as `new`, `viral-risk`, `weak-verification`, `social-only`, `access-unclear`, or `watch`.
- Keep social-only or single-post items out of `Strong Finds` unless independently verified.
- For high-impact domains, make the caveat stronger rather than deleting every trend signal.

## Candidate Judge

Score each serious candidate on a 100-point scale:

- Relevance: 0-30
- Evidence: 0-20
- Freshness: 0-15
- Novelty versus archive: 0-15
- Adoption signal: 0-10
- Safety/trust: 0-10

Grades:

- A: 80-100, recommend in the main answer
- B: 65-79, mention as a candidate
- C: 50-64, optional/appendix only
- Reject: under 50, omit or summarize as rejected

## Caps And Downgrades

- Single X/Threads post without external evidence cannot exceed B.
- Single viral social post with no URL, date, or author cannot exceed C.
- Candidate with no official repo/docs/demo cannot exceed B unless the request is specifically about social sentiment.
- Stale fast-moving AI/agentic repos cannot exceed C unless the repo is canonical or intentionally stable.
- Paid-only source access cannot be a blocker unless the user explicitly requested that source.
- Promotional posts get a safety penalty unless independent users report real usage.
- Archive duplicates should be marked as "known" unless there is new evidence, a new release, or a new usage pattern.
- Human-impact recommendations without user-validation or evaluation plan cannot exceed B.
- Sensitive-data candidates without a privacy, consent, and deletion plan cannot exceed C.
- Project ideas without incumbent baseline checks cannot exceed B.
- Reader-proxy-only or browser-session-only candidates without independent evidence cannot exceed B.
- Metadata-only or cache/archive-only candidates cannot exceed C unless the task is explicitly archival.
- Login-required candidates with no readable body cannot exceed C and usually belong in `Access-Limited Leads`.
- Missing access provenance cannot exceed C.

## Rejection Checklist

Reject or downgrade when:

- The result is only adjacent to the user's problem.
- The result is a generic listicle, repost, or SEO page.
- The post claims a tool exists but no repo/docs/product can be found.
- Engagement appears driven by controversy rather than practical usefulness.
- The source is stale for the relevant ecosystem.
- The result mostly duplicates something already in the archive.
- The candidate requires broad credentials, cookie export, or risky scraping for little value.

## Skeptic Pass

Before answering, ask:

- What problem does this candidate solve for the user?
- What evidence would fail if the social post were deleted?
- Is there a working artifact, repo, docs page, or demo?
- Is the author incentivized to exaggerate?
- Did the scout over-attend to X/Threads because the content was vivid?
- Is this actually new relative to the user's archive?
- For human-impact domains, what affected-user evidence or validation plan is missing?
- For project ideas, which incumbent already solves most of the problem?
- What remains true if the reader-proxy result, browser session, or social post disappears?
- Is the access method strong enough for the section where the candidate is being placed?
