#!/usr/bin/env python3
"""Score RadarX candidates.

Input JSON can be either a list of candidates or {"candidates": [...]}.
Each candidate may include:
  name, url, sources, relevance, evidence, freshness, novelty, adoption, safety,
  volatile_social_only, external_evidence, missing_provenance, stale_fast_moving,
  human_impact_no_user_validation, sensitive_data_no_privacy_plan,
  project_idea_no_baseline_check.
"""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any


MAXIMA = {
    "relevance": 30,
    "evidence": 20,
    "freshness": 15,
    "novelty": 15,
    "adoption": 10,
    "safety": 10,
}


def clamp_score(value: Any, maximum: int) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError):
        number = 0.0
    return max(0.0, min(float(maximum), number))


def grade(total: float) -> str:
    if total >= 80:
        return "A"
    if total >= 65:
        return "B"
    if total >= 50:
        return "C"
    return "Reject"


def score_candidate(candidate: dict[str, Any]) -> dict[str, Any]:
    scores = {key: clamp_score(candidate.get(key), maximum) for key, maximum in MAXIMA.items()}
    total = sum(scores.values())
    cap_reasons: list[str] = []

    volatile = bool(candidate.get("volatile_social_only"))
    external_evidence = bool(candidate.get("external_evidence"))
    missing_provenance = bool(candidate.get("missing_provenance"))
    stale_fast_moving = bool(candidate.get("stale_fast_moving"))
    human_impact_no_user_validation = bool(candidate.get("human_impact_no_user_validation"))
    sensitive_data_no_privacy_plan = bool(candidate.get("sensitive_data_no_privacy_plan"))
    project_idea_no_baseline_check = bool(candidate.get("project_idea_no_baseline_check"))

    if volatile and not external_evidence and total > 79:
        total = 79
        cap_reasons.append("volatile social-only candidate without external evidence cannot exceed B")
    if missing_provenance and total > 64:
        total = 64
        cap_reasons.append("missing provenance cannot exceed C")
    if stale_fast_moving and total > 64:
        total = 64
        cap_reasons.append("stale fast-moving ecosystem candidate cannot exceed C")
    if human_impact_no_user_validation and total > 79:
        total = 79
        cap_reasons.append("human-impact candidate without user validation cannot exceed B")
    if sensitive_data_no_privacy_plan and total > 64:
        total = 64
        cap_reasons.append("sensitive-data candidate without privacy plan cannot exceed C")
    if project_idea_no_baseline_check and total > 79:
        total = 79
        cap_reasons.append("project idea without incumbent baseline check cannot exceed B")

    return {
        **candidate,
        "scores": scores,
        "total": round(total, 2),
        "grade": grade(total),
        "cap_reasons": cap_reasons,
    }


def load_candidates(path: str | None) -> list[dict[str, Any]]:
    raw = sys.stdin.read() if path in (None, "-") else open(path, encoding="utf-8").read()
    parsed = json.loads(raw)
    candidates = parsed.get("candidates") if isinstance(parsed, dict) else parsed
    if not isinstance(candidates, list):
        raise SystemExit("Input must be a JSON array or an object with a candidates array.")
    if not all(isinstance(item, dict) for item in candidates):
        raise SystemExit("Every candidate must be a JSON object.")
    return candidates


def render_markdown(scored: list[dict[str, Any]]) -> str:
    lines = [
        "| Grade | Score | Candidate | Cap Reasons |",
        "|---|---:|---|---|",
    ]
    for item in sorted(scored, key=lambda row: row["total"], reverse=True):
        name = str(item.get("name") or item.get("url") or "(unnamed)").replace("|", "\\|")
        reasons = "; ".join(item.get("cap_reasons") or [])
        lines.append(f"| {item['grade']} | {item['total']} | {name} | {reasons} |")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", help="JSON input file. Use stdin when omitted or '-'.")
    parser.add_argument("--format", choices=["json", "markdown"], default="json")
    args = parser.parse_args()

    scored = [score_candidate(candidate) for candidate in load_candidates(args.input)]
    scored.sort(key=lambda row: row["total"], reverse=True)

    if args.format == "markdown":
        print(render_markdown(scored), end="")
    else:
        print(json.dumps({"candidates": scored}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
