# Output Contract

Use this shape unless the user asks for a smaller answer.

## Short Form

```markdown
**Intent**
<what the user is trying to discover and what counts as useful>

**Attention Mode**
<quick|balanced|deep|social-heavy|archive-first> - <why>

**Archive Connections**
- <known related archive item, topic, author, or gap>

**Access Coverage**
- <archive/public-web/reader-proxy/public-api/browser-session/paid-api availability and any material gaps>

**Strong Finds**
| Grade | Candidate | Why It Matters | Evidence | Caveat |
|---|---|---|---|---|
| A/B | <name> | <fit> | <URLs, source types, access quality> | <risk or unknown> |

**Trending Signals**
- <0-3 fresh high-fit signals, including weak or empty result when none qualify; label with tags such as `new`, `viral-risk`, `weak-verification`, `social-only`, `access-unclear`, or `watch`>

**Access-Limited Leads**
- <high-fit leads with partial metadata, reader-proxy-only, browser-session-only, cache/archive, login-required, or failed-access caveats>

**Rejected Or Weak Signals**
- <what was ignored and why>

**Next Searches**
- <queries, communities, authors, repos, or APIs to try next>
```

## Research Brief Form

Use this form for project ideas, contest entries, MVP planning, or "what information do I need?" requests.

```markdown
**Intent**
<project idea, beneficiary, context, and what useful research means>

**Attention Mode**
<mode> - <why, including human-impact gates when relevant>

**Archive Connections**
- <related saved material, adjacent pattern, or explicit archive gap>

**Access Coverage**
- <archive/public-web/reader-proxy/public-api/browser-session/paid-api availability and any material gaps>

**Baseline Reality**
- <existing products, workflows, standards, or incumbents the idea must beat or complement>

**Strong Finds**
| Grade | Candidate | Use In This Project | Evidence | Caveat |
|---|---|---|---|---|
| A/B | <API/repo/standard/product/community> | <MVP/research/evaluation use> | <URLs, source types, access quality> | <risk or unknown> |

**Recommended Build Path**
- `v1`: <smallest testable version>
- `v1.5`: <near-term additions>
- `v2/defer`: <high-risk or later features>

**Evaluation Plan**
- <metrics, test data, user validation, and failure labels>

**Risk Gates**
- <privacy, consent, accessibility, safety, cost, policy, or operational risks>

**Trending Signals**
- <0-3 fresh high-fit signals, including weak or empty result when none qualify; label with tags such as `new`, `viral-risk`, `weak-verification`, `social-only`, `access-unclear`, or `watch`>

**Access-Limited Leads**
- <high-fit leads with partial metadata, reader-proxy-only, browser-session-only, cache/archive, login-required, or failed-access caveats>

**Rejected Or Weak Signals**
- <what was ignored and why>

**Next Searches**
- <queries, communities, authors, repos, APIs, or datasets to inspect next>
```

## Candidate Fields

Capture these fields during the scout:

- `name`
- `url`
- `kind`: repo, post, discussion, video, paper, product, workflow, person
- `sources`: github, reddit, hn, youtube, x, threads, bluesky, web, archive
- `access_method`: original, public-api, reader-proxy, metadata-only, cache-archive, browser-session, paid-api, login-required, or failed
- `access_quality`: full-original, full-public-api, full-reader-proxy, full-browser-session, partial-metadata, cache-archive, login-required, or failed
- `provenance_note`: short note about how the candidate was accessed and what was missing
- `corroborating_sources`: independent sources that validate the same candidate or claim
- `problem_fit`
- `evidence_summary`
- `archive_connection`
- `scores`: relevance, evidence, freshness, novelty, adoption, safety
- `grade`
- `caveats`
- `recommended_action`: inspect, watch, archive, skip, setup-needed
- `baseline_role`: incumbent, dependency, evaluation_source, community_signal, or stretch_feature
- `mvp_tier`: v1, v1.5, v2, defer
- `risk_flags`: privacy, consent, accessibility, safety, cost, licensing, stale, social-only
  - add `trending`, `viral-risk`, `weak-verification`, `reader-proxy-only`, `browser-session-only`, `metadata-only`, `cache-archive-only`, `login-required`, or `access-limited` when relevant

## Citation Rules

- Cite URLs for every A/B candidate.
- Separate archive evidence from live evidence.
- Label X/Threads-only evidence as `social-only` and keep it in `Trending Signals` unless it has independent validation.
- Label access method for reader-proxy, browser-session, metadata-only, cache/archive, and login-required candidates.
- Do not imply comments, replies, or sentiment are comprehensive unless the source supports that.
- If exact dates or freshness matter, include absolute dates.
- Separate baseline products from recommended build dependencies.
- For human-impact domains, do not present social posts as sufficient evidence.

## Negative Result

When results are weak, say:

```markdown
I did not find strong live candidates. The best signals were weak because <reasons>. The next useful search would be <query/source>.
```

This is better than padding the answer with low-signal links.

Still include `Trending Signals` with either 1-3 labeled weak-but-relevant items or a short note that no relevant trend signal qualified.
If access was the blocker, include `Access-Limited Leads` with the attempted route and the next best access path.
