# 📡 RadarX

한국어 기본 소개 | 🔎 <a href="#english-readme">English README</a>

RadarX는 Codex, Claude Code 같은 코딩 에이전트가 최신 AI 도구, 오픈소스 프로젝트, 에이전트 워크플로, 베스트 프랙티스, 프로젝트 아이디어의 live signal을 포착할 때 쓰는 리서치 스킬입니다.

핵심 목표는 "많이 찾기"가 아니라 "쓸모 있는 후보만 근거 기반으로 걸러내기"입니다. Threads, X 같은 소셜 신호는 빠른 발견에는 유용하지만 단독 근거로는 약하므로, GitHub, 공식 문서, 릴리즈 노트, Reddit/Hacker News 토론, 논문, 데모 같은 독립 근거와 함께 평가합니다.

## 🔎 이런 상황에 씁니다

- "Threads/X/GitHub/Reddit에서 최근 AI 워크플로 사례를 찾아줘."
- "이 AI 공모전 아이디어를 구현하려고 하는데 필요한 정보를 조사해줘."
- "요즘 뜨는 오픈소스 툴 중 실제로 쓸 만한 것만 걸러줘."
- "내가 저장해둔 Threads 아카이브와 연결해서 새 후보를 찾아줘."
- "소셜에서 화제인 도구가 진짜 쓸 만한지 회의적으로 검증해줘."

## 🧭 주요 기능

- 로컬 Threads 아카이브가 있으면 먼저 검색하고, 기존 관심사와 연결합니다.
- GitHub, 공식 문서, Reddit, Hacker News, YouTube, Hugging Face, arXiv, Product Hunt, X, Threads, Bluesky, Mastodon, 웹 검색을 계층적으로 활용합니다.
- 후보를 관련성, 근거, 최신성, 아카이브 대비 새로움, 채택 신호, 안전성으로 점수화합니다.
- 단일 바이럴 포스트, 출처 불명 주장, 오래된 AI repo, 개인정보 계획 없는 민감 데이터 아이디어를 자동으로 낮게 평가합니다.
- 프로젝트 아이디어 리서치에서는 기존 대체재, MVP 경로, 평가 계획, 리스크 게이트까지 함께 정리합니다.
- 강한 후보, 불안정한 소셜 신호, 약해서 버린 후보, 다음 검색어를 분리해서 보고합니다.

## 🧩 사용 조건: X/Threads 로그인이나 브라우저 자동화가 꼭 필요한가요?

아니요. RadarX의 기본 사용에는 X/Threads 로그인, Playwright, browser-use, Chrome 자동화가 필수 아닙니다.

기본 동작은 다음 공개/저마찰 근거만으로도 충분히 가능합니다.

- GitHub repo, release, issue, discussion
- 공식 문서, changelog, API 문서
- Reddit, Hacker News, YouTube transcript, arXiv, Hugging Face, Product Hunt
- 일반 웹 검색
- 사용자의 로컬 Threads archive가 있을 경우 그 archive snapshot

X/Threads 로그인은 선택 사항입니다. 로그인된 브라우저나 공식 API가 있으면 최신 소셜 신호를 더 잘 볼 수 있지만, 없으면 `site:x.com`, `site:threads.com`, GitHub/공식 문서/커뮤니티 검색으로 fallback합니다. 이 경우 답변에는 "X/Threads 직접 검색은 제한됨"이라고 명시하고, 약한 소셜 신호를 강한 근거처럼 포장하지 않습니다.

Playwright, browser-use, Codex Chrome 같은 브라우저 자동화도 선택 사항입니다. 동적 웹페이지, 로그인된 X/Threads, 브라우저 세션이 필요한 조사를 할 때만 도움이 됩니다. 일반적인 리서치 브리프, 오픈소스 탐색, 공식 문서 검증, GitHub 후보 점수화에는 없어도 됩니다.

민감한 세션 쿠키나 토큰을 export해서 쓰는 방식은 권장하지 않습니다. RadarX는 "가능한 공개 근거 먼저, 로그인/유료/브라우저 의존은 보조 adapter"라는 원칙으로 설계되어 있습니다.

## 🗂️ 레포 구조

```text
skills/radarx/
  SKILL.md
  agents/openai.yaml
  references/
    attention-policy.md
    output-contract.md
    research-brief-playbook.md
    source-playbook.md
  scripts/
    score_candidates.py
install.sh
```

## ⚡ 빠른 설치

### Codex

Codex에 `skill-installer`가 있으면 GitHub에서 바로 설치할 수 있습니다.

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo Oscar-V4/radarx-skill \
  --path skills/radarx
```

설치 후 Codex를 재시작하면 스킬이 인식됩니다.

수동 설치:

```bash
git clone https://github.com/Oscar-V4/radarx-skill.git
mkdir -p ~/.codex/skills
cp -R radarx-skill/skills/radarx ~/.codex/skills/radarx
```

설치 스크립트 사용:

```bash
git clone https://github.com/Oscar-V4/radarx-skill.git
cd radarx-skill
./install.sh --target codex
```

### Claude Code

Claude Code는 개인 스킬을 `~/.claude/skills/<skill-name>/SKILL.md`에서, 프로젝트 스킬을 `.claude/skills/<skill-name>/SKILL.md`에서 인식합니다. 공식 문서: <https://docs.claude.com/en/docs/claude-code/skills>

개인 스킬로 설치:

```bash
git clone https://github.com/Oscar-V4/radarx-skill.git
mkdir -p ~/.claude/skills
cp -R radarx-skill/skills/radarx ~/.claude/skills/radarx
```

설치 스크립트 사용:

```bash
git clone https://github.com/Oscar-V4/radarx-skill.git
cd radarx-skill
./install.sh --target claude
```

설치 후 Claude Code를 재시작하세요.

## 📡 사용 예시

Codex:

```text
$radarx 실시간 AI 음성 에이전트에 쓸 만한 최근 오픈소스 툴을 찾아줘.
```

Claude Code:

```text
Use radarx to research my AI hackathon idea and reject weak social hype.
```

한국어로 자연스럽게 요청해도 됩니다.

```text
학교 AI 공모전에 낼 청각장애 학우용 음성인식+AI툴 아이디어를 조사해줘.
```

## 📌 기본 출력 형식

보통 다음 항목으로 답합니다.

- Intent: 사용자가 풀려는 문제와 좋은 후보의 기준
- Attention Mode: quick, balanced, deep, social-heavy, archive-first 중 선택
- Archive Connections: 기존 아카이브와의 연결점
- Baseline Reality: 프로젝트 아이디어일 때 기존 제품/대체재
- Strong Finds: 근거가 강한 후보
- Recommended Build Path: MVP, v1.5, v2/defer
- Evaluation Plan: 정확도, 지연시간, 사용자 검증, 실패 라벨
- Risk Gates: 개인정보, 동의, 접근성, 안전성, 비용, 정책 리스크
- Volatile Social Signals: 아직 검증이 약한 소셜 신호
- Rejected Or Weak Signals: 버린 후보와 이유
- Next Searches: 다음에 더 파볼 검색어/커뮤니티/문서

## 🧠 에이전트를 위한 가이드라인

이 스킬을 사용하는 에이전트는 다음 순서를 따르는 것이 좋습니다.

1. `skills/radarx/SKILL.md`를 먼저 읽습니다.
2. `references/attention-policy.md`에서 attention mode를 고릅니다.
3. "이걸 만들고 싶다", "필요한 정보를 조사해줘" 유형이면 `references/research-brief-playbook.md`를 읽습니다.
4. 로컬 Threads 아카이브가 있으면 먼저 검색하되, 아카이브 근거와 최신 라이브 근거를 분리해서 표시합니다.
5. X/Threads보다 공식 문서, GitHub repo, 릴리즈 노트, 재현 가능한 데모, 고신뢰 커뮤니티 토론을 우선합니다.
6. X, Threads, Bluesky, Mastodon 결과는 독립 근거가 없으면 volatile signal로만 취급합니다.
7. 후보가 많거나 판단이 애매하면 `scripts/score_candidates.py`로 점수화합니다.
8. A/B 후보에는 URL을 반드시 붙입니다.
9. 출처 불명, 약한 근거, 오래된 repo, 개인정보 계획 부재, 기존 대체재 검토 부재는 점수를 낮춥니다.
10. 강한 후보가 없으면 억지로 채우지 말고 "강한 후보 없음"이라고 말합니다.
11. X/Threads 로그인이나 브라우저 자동화가 없으면 공개 검색 fallback을 쓰고, 그 한계를 답변에 명시합니다.

## ⚖️ 점수화 도우미

```bash
python3 skills/radarx/scripts/score_candidates.py --format markdown <<'JSON'
{
  "candidates": [
    {
      "name": "Example repo-backed candidate",
      "relevance": 28,
      "evidence": 18,
      "freshness": 14,
      "novelty": 12,
      "adoption": 8,
      "safety": 8,
      "external_evidence": true
    }
  ]
}
JSON
```

## 📄 라이선스

MIT

<details id="english-readme">
<summary>English README</summary>

# 📡 RadarX

Archive-aware, evidence-gated research skill for finding useful AI tools, open-source projects, agentic workflows, best practices, and project-idea signals across live social/community sources and reliable public sources.

RadarX is designed for agents that need to answer questions like:

- "Find recent AI workflow examples from Threads/X/GitHub/Reddit."
- "I want to build this AI project. What information do I need?"
- "Scout open-source tools and reject noisy social hype."
- "Connect new findings to my existing personal Threads archive."

The skill favors a small number of useful, source-backed candidates over broad recall. It treats X/Threads as volatile discovery surfaces, not standalone proof.

## 🔎 What It Does

- Searches local archive context first when available.
- Fans out to GitHub, official docs, Reddit, Hacker News, YouTube, Hugging Face, arXiv, Product Hunt, X, Threads, Bluesky, Mastodon, and web sources.
- Scores candidates by relevance, evidence, freshness, novelty, adoption, and safety.
- Downgrades weak social-only signals, stale repos, missing provenance, and sensitive-data ideas without privacy plans.
- Produces structured research briefs with strong finds, volatile signals, rejected weak signals, and next searches.
- Handles project-idea research with baseline checks, MVP paths, evaluation plans, and risk gates.

## 🧩 Requirements And Optional Adapters

RadarX does not require X/Threads login, Playwright, browser-use, or Chrome automation for normal use.

The core workflow works with public and low-friction sources:

- GitHub repositories, releases, issues, and discussions
- Official docs, changelogs, and API docs
- Reddit, Hacker News, YouTube transcripts, arXiv, Hugging Face, Product Hunt
- General web search
- A local Threads archive snapshot, when available

X/Threads login is optional. A logged-in browser or official API can improve fresh social discovery, but RadarX should fall back to public search such as `site:x.com`, `site:threads.com`, GitHub, official docs, and community sources when those adapters are unavailable.

Playwright, browser-use, and Codex Chrome are optional adapters for dynamic or logged-in pages. They are not required for ordinary research briefs, open-source scouting, official-doc verification, or candidate scoring.

Do not export cookies or tokens just to use RadarX. If a source is unavailable, say so and continue with public evidence.

## ⚡ Quick Install

### Codex

If your Codex installation includes `skill-installer`, install directly from GitHub:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo Oscar-V4/radarx-skill \
  --path skills/radarx
```

Then restart Codex so the new skill is discovered.

Manual install:

```bash
git clone https://github.com/Oscar-V4/radarx-skill.git
mkdir -p ~/.codex/skills
cp -R radarx-skill/skills/radarx ~/.codex/skills/radarx
```

Or use the installer script:

```bash
git clone https://github.com/Oscar-V4/radarx-skill.git
cd radarx-skill
./install.sh --target codex
```

### Claude Code

Claude Code discovers personal skills from `~/.claude/skills/<skill-name>/SKILL.md` and project skills from `.claude/skills/<skill-name>/SKILL.md`. See the official Claude Code skills docs: <https://docs.claude.com/en/docs/claude-code/skills>

Install as a personal Claude Code skill:

```bash
git clone https://github.com/Oscar-V4/radarx-skill.git
mkdir -p ~/.claude/skills
cp -R radarx-skill/skills/radarx ~/.claude/skills/radarx
```

Or use the installer script:

```bash
git clone https://github.com/Oscar-V4/radarx-skill.git
cd radarx-skill
./install.sh --target claude
```

Restart Claude Code after installation.

## 🧠 Agent Guidelines

When using this skill as an AI agent:

1. Load `skills/radarx/SKILL.md` first.
2. Use `references/attention-policy.md` to choose quick, balanced, deep, social-heavy, or archive-first mode.
3. For "I want to build..." or "what information do I need?" prompts, load `references/research-brief-playbook.md`.
4. Search local archive snapshots first when available, but label them as archive context rather than live evidence.
5. Prefer official docs, GitHub repos, release notes, reproducible demos, and high-signal community discussions before X/Threads.
6. Treat X/Threads/Bluesky/Mastodon as volatile candidate discovery unless independent evidence exists.
7. Run `scripts/score_candidates.py` for larger candidate sets or when a deterministic ranking is useful.
8. Include URLs for A/B candidates.
9. Downgrade candidates with missing provenance, weak evidence, stale activity, privacy gaps, or no baseline comparison.
10. It is acceptable to report that no strong live candidates were found.
11. If X/Threads login or browser automation is unavailable, use public fallback sources and label the limitation.

## 📄 License

MIT

</details>
