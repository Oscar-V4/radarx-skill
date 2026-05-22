# 📡 RadarX

<p align="center">
  <b>한국어</b> |
  <a href="docs/README.en.md">English</a> |
  <a href="docs/README.zh-CN.md">简体中文</a>
</p>

**RadarX는 최신 AI, 오픈소스, 소셜, 커뮤니티 신호를 잡아내는 레이더형 에이전트 스킬입니다.**  
Threads, X, Reddit, Hacker News, GitHub, YouTube, Hugging Face, arXiv, Product Hunt 같은 live source를 훑되, 약한 바이럴 신호는 걸러내고 근거가 있는 후보만 작게 추려줍니다.

- 최신 AI 도구, 오픈소스 프로젝트, agentic workflow, best practice 신호를 찾습니다.
- 로컬 Threads archive가 있으면 먼저 연결하고, 새 live signal과 분리해서 표시합니다.
- GitHub, 공식 문서, Reddit/HN, YouTube, arXiv, Hugging Face, Product Hunt, 웹 검색을 계층적으로 사용합니다.
- 후보를 관련성, 근거, 최신성, 새로움, 채택 신호, 안전성으로 점수화합니다.
- 소셜에서 뜬 주장이라도 독립 근거가 약하면 `volatile` 또는 `rejected`로 낮춥니다.
- 프로젝트 아이디어는 기존 대체재, MVP 경로, 평가 계획, 리스크 게이트까지 함께 봅니다.

## 빠른 설치

친구에게 공유할 때는 아래 프롬프트를 그대로 복사해서 Codex, Claude Code, Antigravity 같은 에이전트에게 붙여넣으면 됩니다.

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
- **Strong Finds**: 근거가 강한 후보와 URL
- **Volatile Social Signals**: 아직 독립 검증이 약한 live/social 신호
- **Rejected Or Weak Signals**: 버린 후보와 이유
- **Next Searches**: 다음에 더 파볼 검색어, 커뮤니티, 문서

프로젝트 아이디어나 MVP 조사에서는 기존 대체재, build path, 평가 계획, privacy/safety risk gate까지 확장합니다.

## 에이전트 호환성

이 repo는 `SKILL.md` 기반 에이전트 스킬 구조로 패키징되어 있습니다. Codex와 Claude Code처럼 사용자 스킬 폴더를 읽는 에이전트에서는 그대로 설치할 수 있고, 다른 에이전트에서도 `skills/radarx/SKILL.md`를 읽게 하면 같은 지침으로 활용할 수 있습니다.

에이전트마다 스킬 자동 로딩 규칙은 다를 수 있으므로, 가장 확실한 방식은 위의 “빠른 설치” 프롬프트를 에이전트에게 붙여넣고 현재 환경에 맞게 설치하게 하는 것입니다.

## 사용 조건

RadarX는 X/Threads 로그인, Playwright, browser-use, Chrome 자동화, 유료 scraping API가 없어도 동작합니다. 가능한 공개 근거를 먼저 쓰고, 로그인/유료/브라우저 의존 source는 선택적 adapter로 취급합니다.

민감한 세션 쿠키나 토큰을 export해서 쓰는 방식은 권장하지 않습니다. 어떤 source가 제한되면 답변에 한계를 표시하고 공개 fallback으로 진행합니다.

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
