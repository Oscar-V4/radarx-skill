<p align="center">
  <img src="assets/radarx-logo.png" alt="RadarX logo" width="172">
</p>

# RadarX

<p align="center">
  <b>한국어</b> |
  <a href="docs/README.en.md">English</a> |
  <a href="docs/README.zh-CN.md">简体中文</a>
</p>

**RadarX는 최신 AI, 오픈소스, 소셜, 커뮤니티 신호를 잡아내는 레이더형 리서치 스킬입니다.**  
Threads, X, Reddit, Hacker News, GitHub, YouTube, Hugging Face, arXiv, Product Hunt 같은 live source를 훑되, 공개 접근 사다리와 provenance 태깅으로 막힌 웹 게시물까지 최대한 읽고, 검증된 추천과 약한 트렌딩 신호를 분리합니다.

- 최신 AI 도구, 오픈소스 프로젝트, agentic workflow, best practice 신호를 찾습니다.
- 로컬 Threads archive가 있으면 먼저 연결하고, 새 live signal과 분리해서 표시합니다.
- GitHub, 공식 문서, Reddit/HN, YouTube, arXiv, Hugging Face, Product Hunt, 웹 검색을 계층적으로 사용합니다.
- 일반 브라우징이 막힌 URL은 `r.jina.ai`, public API, RSS/feed, metadata, cache/archive, optional browser session 순서로 접근합니다.
- 후보를 관련성, 근거, 최신성, 새로움, 채택 신호, 안전성으로 점수화합니다.
- 소셜에서 뜬 주장이라도 독립 근거가 약하면 `Trending Signals`나 `Access-Limited Leads`로 분리합니다.
- reader-proxy, metadata-only, cache/archive, login-required 결과가 과대 추천되지 않도록 access-quality cap을 적용합니다.
- 프로젝트 아이디어는 기존 대체재, MVP 경로, 평가 계획, 리스크 게이트까지 함께 봅니다.

## 빠른 설치

아래 프롬프트를 그대로 복사해서 Codex, Claude Code, Antigravity 같은 에이전트에게 붙여넣으세요.

```text
이 GitHub repo를 확인해서 RadarX 에이전트 스킬을 설치해줘:
https://github.com/Oscar-V4/radarx-skill

현재 네가 실행 중인 에이전트 환경을 감지해서 설치해.
- Codex 계열이면 ~/.codex/skills/radarx 에 설치해.
- Claude Code 계열이면 ~/.claude/skills/radarx 에 설치해.
- 다른 에이전트면 SKILL.md 기반 스킬 폴더를 지원하는지 확인하고, 가장 가까운 사용자 스킬 위치에 설치해.
- 전용 설치기가 있으면 사용하고, 없으면 repo를 clone한 뒤 skills/radarx 폴더를 사용자 스킬 디렉터리에 복사해.

설치 후 skills/radarx/SKILL.md와 README.md를 읽고,
1. 언제 $radarx를 쓰면 좋은지
2. 어떤 식으로 말하면 좋은지
3. 첫 테스트 프롬프트 3개
를 간단히 알려줘.
```

직접 설치할 때:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo Oscar-V4/radarx-skill \
  --path skills/radarx
```

설치 후 에이전트 앱을 재시작하면 `$radarx`로 호출할 수 있습니다.

## 언제 쓰면 좋은가

| 상황 | 이렇게 말하면 됩니다 |
|---|---|
| 최신 AI/오픈소스 흐름을 보고 싶을 때 | `$radarx 최근 AI 음성 에이전트에 쓸 만한 오픈소스 툴을 찾아줘.` |
| 소셜에서 화제인 도구가 진짜인지 보고 싶을 때 | `$radarx X/Threads에서 뜨는 이 도구가 실제로 쓸 만한지 근거 기반으로 검증해줘.` |
| 공모전/해커톤 아이디어를 조사할 때 | `$radarx 이 AI 공모전 아이디어에 필요한 정보, 기존 대체재, MVP 경로를 조사해줘.` |
| 내 archive와 연결해 새 후보를 찾고 싶을 때 | `$radarx 내 Threads archive와 연결해서 비슷하지만 새로운 AI workflow 사례를 찾아줘.` |
| 약한 링크를 많이 받기 싫을 때 | `$radarx 강한 후보만 3개 이하로 추리고, 버린 후보와 이유도 알려줘.` |
| live social coverage가 중요할 때 | `$radarx social-heavy 모드로 X, Threads, Reddit, HN 신호를 먼저 훑어줘.` |

## 결과물은 어떻게 나오나

RadarX는 보통 아래처럼 답합니다.

- **Intent**: 사용자가 풀려는 문제와 좋은 후보의 기준
- **Attention Mode**: quick, balanced, deep, social-heavy, archive-first 중 선택
- **Archive Connections**: 기존 archive와의 연결점
- **Access Coverage**: archive, public web, reader-proxy, public API, browser session 등의 접근 범위
- **Strong Finds**: 근거가 강한 후보와 URL
- **Trending Signals**: 최신·고적합이지만 검증이 약한 신호
- **Access-Limited Leads**: 본문 일부, reader-proxy-only, metadata-only, cache/archive, login-required 후보
- **Rejected Or Weak Signals**: 버린 후보와 이유
- **Next Searches**: 다음에 더 파볼 검색어, 커뮤니티, 문서

프로젝트 아이디어나 MVP 조사에서는 기존 대체재, build path, 평가 계획, privacy/safety risk gate까지 확장합니다.

## 에이전트 호환성

이 repo는 `SKILL.md` 기반 에이전트 스킬 구조로 패키징되어 있습니다. Codex와 Claude Code처럼 사용자 스킬 폴더를 읽는 에이전트에서는 그대로 설치할 수 있고, 다른 에이전트에서도 `skills/radarx/SKILL.md`를 읽게 하면 같은 지침으로 활용할 수 있습니다.

에이전트마다 스킬 자동 로딩 규칙은 다를 수 있으므로, 가장 확실한 방식은 위의 “빠른 설치” 프롬프트를 에이전트에게 붙여넣고 현재 환경에 맞게 설치하게 하는 것입니다.

## 사용 조건

RadarX는 X/Threads 로그인, Playwright, browser-use, Chrome 자동화, 유료 scraping API가 없어도 동작합니다. 가능한 공개 근거를 먼저 쓰고, 로그인/유료/브라우저 의존 source는 선택적 enhanced adapter로 취급합니다.

브라우저 플러그인이나 로그인 세션이 있는 환경에서는 더 많은 live/social 정보를 확인할 수 있지만, 결과에는 항상 `access_method`, `access_quality`, `provenance_note`를 남기는 방향으로 동작합니다.

민감한 세션 쿠키나 토큰을 export해서 쓰는 방식은 권장하지 않습니다. 어떤 source가 제한되면 답변에 한계를 표시하고 공개 fallback으로 진행합니다.

## 스킬 전문

<details>
<summary><code>skills/radarx/SKILL.md</code> 전문 보기</summary>

````markdown
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

When a user has browser plugins, logged-in sessions, Playwright, or paid/social APIs available, RadarX may use them as enhanced adapters. They expand coverage but do not replace provenance labels, source skepticism, or the public fallback path.

## Core Rule

Maximize useful, archive-aware, evidence-backed discovery by aggressively rejecting weak live social signals.

Never let X/Threads virality override weak relevance or weak evidence. Treat "no strong live candidates found" as a successful outcome.

Always include a compact `Trending Signals` section in the report. Use it for 0-3 fresh, highly relevant candidates that may be viral, early, or weakly verified but are worth the user's attention. Label them plainly, for example `new`, `viral-risk`, `weak-verification`, `social-only`, `access-unclear`, or `watch`. Do not mix these with `Strong Finds`, and do not present them as validated recommendations.

For every serious candidate, preserve access provenance: how the content was reached, whether it was full text or partial metadata, and what would remain if the social/browser view disappeared. Use provenance to decide whether the candidate belongs in `Strong Finds`, `Trending Signals`, or `Access-Limited Leads`.

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
   - For blocked or dynamic public URLs, follow the Public Web Access Ladder in `references/source-playbook.md` before giving up or escalating to browser automation.
   - Paid or credentialed sources must stay optional and best-effort unless the user explicitly requests setup.
   - Load `references/source-playbook.md` for source-specific tactics and fallback order.

5. Score candidates before synthesizing.
   - Use the Evidence Ladder and Candidate Judge in `references/attention-policy.md`.
   - Apply access-quality caps from `references/attention-policy.md` so reader-proxy, metadata-only, cache/archive, browser-session-only, and login-required leads are not over-promoted.
   - For larger result sets, write a temporary JSON candidate list outside project repos and run `scripts/score_candidates.py`.
   - Only A/B candidates belong in the main answer.

6. Run the skeptic pass.
   - Ask whether each strong candidate is just promotion, SEO, a single viral post, stale, already in the archive, unsupported by code/docs, or unrelated to the user's actual problem.
   - Downgrade or reject anything that fails.
   - Preserve fresh high-fit items as `Trending Signals` when they fail validation but still look useful to know about.

7. Report using the output contract.
   - Separate `Strong Finds`, `Trending Signals`, `Access-Limited Leads`, `Archive Connections`, `Rejected/Weak Signals`, and `Next Searches`.
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

Good outputs still surface a tiny number of relevant trend signals, even when evidence is weak, as long as they are clearly labeled and separated from recommendations.

## Resources

- `references/attention-policy.md`: attention modes, evidence ladder, scoring rubric, social caps, rejection rules.
- `references/source-playbook.md`: source adapters, query tactics, fallback order, and setup friction.
- `references/output-contract.md`: answer format and candidate fields.
- `references/research-brief-playbook.md`: project-idea and "needed information" research workflow, baselines, evaluation, and human-impact gates.
- `scripts/score_candidates.py`: deterministic candidate scoring helper for larger scans.
````

</details>

## 저장소 구조

```text
radarx-skill/
├── README.md
├── docs/
│   ├── README.en.md
│   └── README.zh-CN.md
├── install.sh
└── skills/
    └── radarx/
        ├── SKILL.md
        ├── agents/
        │   └── openai.yaml
        ├── references/
        │   ├── attention-policy.md
        │   ├── output-contract.md
        │   ├── research-brief-playbook.md
        │   └── source-playbook.md
        └── scripts/
            └── score_candidates.py
```
