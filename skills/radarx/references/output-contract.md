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

**Strong Finds**
| Grade | Candidate | Why It Matters | Evidence | Caveat |
|---|---|---|---|---|
| A/B | <name> | <fit> | <URLs and source types> | <risk or unknown> |

**Volatile Social Signals**
- <X/Threads/social signal that is fresh but not fully verified>

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

**Baseline Reality**
- <existing products, workflows, standards, or incumbents the idea must beat or complement>

**Strong Finds**
| Grade | Candidate | Use In This Project | Evidence | Caveat |
|---|---|---|---|---|
| A/B | <API/repo/standard/product/community> | <MVP/research/evaluation use> | <URLs and source types> | <risk or unknown> |

**Recommended Build Path**
- `v1`: <smallest testable version>
- `v1.5`: <near-term additions>
- `v2/defer`: <high-risk or later features>

**Evaluation Plan**
- <metrics, test data, user validation, and failure labels>

**Risk Gates**
- <privacy, consent, accessibility, safety, cost, policy, or operational risks>

**Volatile Social Signals**
- <fresh social/community signal, if any, labeled as unverified>

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

## Citation Rules

- Cite URLs for every A/B candidate.
- Separate archive evidence from live evidence.
- Label X/Threads-only evidence as volatile.
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
