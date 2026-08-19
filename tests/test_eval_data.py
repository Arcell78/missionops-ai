import json
from pathlib import Path

def _load():
    path = Path(__file__).resolve().parents[1] / "evals" / "incidents.json"
    return json.loads(path.read_text(encoding="utf-8"))

def test_eval_dataset_has_30_cases():
    assert len(_load()) == 30

def test_eval_case_ids_are_unique():
    ids = [case["id"] for case in _load()]
    assert len(ids) == len(set(ids))
