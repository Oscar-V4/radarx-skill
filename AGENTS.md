# Agent Guidelines

This repository packages one reusable skill: `skills/radarx`.

When maintaining this repo:

- Keep `skills/radarx/SKILL.md` concise and route detailed guidance to one-level-deep files under `references/`.
- Do not place README, changelog, or install docs inside the skill directory.
- Keep install/user documentation at the repository root.
- Validate the skill after edits:

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/radarx
```

When using the skill:

- Load `skills/radarx/SKILL.md`.
- Load `references/research-brief-playbook.md` for project-idea or contest-entry research.
- Use official docs and GitHub evidence before volatile social posts.
- Label X/Threads-only evidence as volatile.
- Run `scripts/score_candidates.py` for larger candidate sets.
- Report weak or empty results directly instead of padding with low-signal links.
