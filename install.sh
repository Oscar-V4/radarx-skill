#!/usr/bin/env bash
set -euo pipefail

target="codex"
force="false"

usage() {
  cat <<'EOF'
Usage: ./install.sh [--target codex|claude] [--force]

Installs skills/radarx into:
  codex  -> ${CODEX_HOME:-$HOME/.codex}/skills/radarx
  claude -> $HOME/.claude/skills/radarx
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --target)
      target="${2:-}"
      shift 2
      ;;
    --force)
      force="true"
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
skill_src="$repo_root/skills/radarx"

if [[ ! -f "$skill_src/SKILL.md" ]]; then
  echo "Missing skill source: $skill_src/SKILL.md" >&2
  exit 1
fi

case "$target" in
  codex)
    base="${CODEX_HOME:-$HOME/.codex}/skills"
    ;;
  claude)
    base="$HOME/.claude/skills"
    ;;
  *)
    echo "Invalid target: $target" >&2
    usage >&2
    exit 2
    ;;
esac

dest="$base/radarx"
mkdir -p "$base"

if [[ -e "$dest" ]]; then
  if [[ "$force" != "true" ]]; then
    echo "Destination already exists: $dest" >&2
    echo "Re-run with --force to replace it." >&2
    exit 1
  fi
  rm -rf "$dest"
fi

cp -R "$skill_src" "$dest"

echo "Installed radarx to $dest"
echo "Restart your agent app so it discovers the skill."
