# Contributing

This repository is primarily a public learning and portfolio project.

## Principles

1. Start with the problem, not the technique.
2. Keep production side effects disabled unless the phase explicitly requires them.
3. Add complexity only when a requirement and an eval justify it.
4. Use synthetic/public data only.
5. Add or update representative eval cases for behavior changes.

## Development

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
pip install -e .
pytest
ruff check .
```
