from __future__ import annotations
import json
import statistics
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from missionops.triage import triage_incident  # noqa: E402

DATASET = REPO_ROOT / "evals" / "incidents.json"
RESULTS_DIR = REPO_ROOT / "evals" / "results"

def exact(value, expected) -> int:
    return int(value == expected)

def main() -> None:
    cases = json.loads(DATASET.read_text(encoding="utf-8"))
    results = []

    for index, case in enumerate(cases, start=1):
        print(f"[{index}/{len(cases)}] {case['id']}")
        observed, latency = triage_incident(case["input"])
        expected = case["expected"]
        results.append({
            "id": case["id"],
            "input": case["input"],
            "expected": expected,
            "observed": observed.model_dump(),
            "latency_seconds": latency,
            "scores": {
                "category": exact(observed.category, expected["category"]),
                "severity": exact(observed.severity, expected["severity"]),
                "escalation_required": exact(
                    observed.escalation_required, expected["escalation_required"]
                ),
                "recommended_action": exact(
                    observed.recommended_action, expected["recommended_action"]
                ),
            },
        })

    def mean_score(field: str) -> float:
        return statistics.mean(r["scores"][field] for r in results)

    summary = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "cases": len(results),
        "category_accuracy": mean_score("category"),
        "severity_accuracy": mean_score("severity"),
        "escalation_accuracy": mean_score("escalation_required"),
        "recommended_action_accuracy": mean_score("recommended_action"),
        "average_latency_seconds": statistics.mean(
            r["latency_seconds"] for r in results
        ),
    }

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out = RESULTS_DIR / f"eval-{stamp}.json"
    out.write_text(
        json.dumps({"summary": summary, "results": results}, indent=2),
        encoding="utf-8",
    )

    print("\nSummary")
    print(json.dumps(summary, indent=2))
    print(f"\nSaved: {out}")

if __name__ == "__main__":
    main()
