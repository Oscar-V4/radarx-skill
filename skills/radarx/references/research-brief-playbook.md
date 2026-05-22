# Research Brief Playbook

Use this reference when the user asks for research to support a project idea, MVP, contest entry, product concept, or "what information do I need?" request.

The goal is a decision-ready research packet, not a link dump.

## Intent Contract

Capture these first:

- User and beneficiary: who benefits, and who actually operates the tool.
- Context: where it will be used, under what constraints, and what failure looks like.
- Job to be done: the practical outcome the user needs, not the technology label.
- Non-goals: impressive but risky features that should not be v1.
- Success threshold: measurable evidence that the idea works well enough.

If the domain affects real people in a sensitive way, use `deep` attention mode.

## Source Order

For project research, use this order before social exploration:

1. Archive connections and gaps.
2. Existing baselines and incumbents.
3. Official standards, platform docs, API docs, and policy pages.
4. Open-source implementations and reproducible demos.
5. Community pain points from users or practitioners.
6. Research papers, benchmarks, datasets, and evaluation methods.
7. X/Threads/other live social signals only as fresh candidate discovery.

Do not recommend building a feature until the incumbent baseline is clear.

## Output Dimensions

Prefer this synthesis shape:

- Problem framing: user, situation, pain, and decision constraint.
- Baselines: existing products or workflows the idea must beat or complement.
- Build paths: fast MVP, privacy/offline path, and stretch path.
- Strong candidates: APIs, repos, datasets, standards, or communities with evidence.
- Differentiation: what makes the idea worth building despite existing tools.
- Evaluation plan: metrics, representative tests, user validation, and failure modes.
- Risk gates: privacy, consent, safety, accessibility, policy, cost, and operational burden.
- Next searches: queries and communities that would improve confidence.

## Human-Impact Gate

Apply this gate for accessibility, disability, education, health, minors, safety, legal, finance, identity, or personal-data workflows.

- Start from official standards or reputable institutional sources, then user/community evidence.
- Avoid stereotypes about the affected group; name uncertainty and individual variation.
- Prefer "co-design/interview with affected users" over assumptions.
- Separate prototype claims from deployable-product claims.
- Include consent, data minimization, deletion, and fallback behavior when audio, video, biometrics, student records, or health data are involved.
- Reject or downgrade candidates that lack a privacy plan when they process sensitive data.

## MVP Split

Classify features as:

- `v1`: required to prove the core value.
- `v1.5`: valuable after the first working demo.
- `v2`: needs more data, integration, or user validation.
- `defer`: high-risk, flashy, or likely to distract.

Strong v1 features should be boring, testable, and visibly useful.

## Evaluation

For technical systems, define at least:

- Task metric: accuracy, latency, recall, cost, throughput, or completion rate.
- Human metric: usefulness, trust, cognitive load, accessibility, or time saved.
- Representative test set: real audio/text/data conditions, not clean demos only.
- Failure labels: empty output, hallucination, delay, truncation, wrong entity, privacy leak, or unsafe suggestion.
- Stop condition: what evidence is enough to choose, skip, or build.

## Skeptic Questions

Before finalizing, ask:

- Is this actually a user problem or just a technology demo?
- Which existing product already solves 70% of it?
- What local context makes the user's version meaningfully better?
- What could harm the intended beneficiary if the model is wrong?
- What evidence would convince a judge, maintainer, or real user?
