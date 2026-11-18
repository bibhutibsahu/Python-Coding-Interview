# Python Coding Interview

[![CI](https://github.com/bibhutibsahu/Python-Coding-Interview/actions/workflows/ci.yml/badge.svg)](https://github.com/bibhutibsahu/Python-Coding-Interview/actions/workflows/ci.yml)
[![Release](https://github.com/bibhutibsahu/Python-Coding-Interview/actions/workflows/release.yml/badge.svg)](https://github.com/bibhutibsahu/Python-Coding-Interview/actions/workflows/release.yml)

Interview practice in Python, pandas, NumPy, SQL (DuckDB) and statistics: notebooks
from real technical rounds plus small, tested scripts.

## Repository layout

| Path | What it is |
|---|---|
| `*.ipynb` | Practice notebooks (many were written in Google Colab) |
| `pareto.py` | Pareto / 80-20 exposure and revenue-crossing helpers |
| `tests/` | Unit tests (pytest) |
| `ci/notebooks-to-execute.txt` | Notebooks that CI runs top-to-bottom |
| `scripts/validate_notebooks.py` | Checks every notebook is a valid `.ipynb` |
| `*.csv` | Small datasets used by the notebooks |
| `docs/` | Tech stack and CI/CD guide (PDF) |
| `.github/` | CI/CD workflows, Dependabot, PR and issue templates |

## Quick start

```bash
git clone git@github.com:bibhutibsahu/Python-Coding-Interview.git
cd Python-Coding-Interview
make setup          # creates .venv, installs deps, installs git hooks
make ci             # runs lint, notebook validation, tests and notebooks
```

In VS Code, pick **Select Kernel → Python Environments → .venv** for the notebooks.

## Make targets

| Command | Does |
|---|---|
| `make setup` | Create `.venv`, install `requirements-dev.txt`, install pre-commit hooks |
| `make lint` / `make format` | Check / auto-fix code style with Ruff |
| `make validate` | Validate every notebook's structure |
| `make test` | Run unit tests |
| `make notebooks` | Execute the curated notebooks |
| `make ci` | All of the above, exactly like CI |

## CI/CD

- **CI** (`.github/workflows/ci.yml`) runs on every push and pull request to `main`:
  lint and format check → notebook validation → tests on Python 3.9–3.12 → curated notebook execution.
- **CD** (`.github/workflows/release.yml`) runs when you push a tag like `v1.0.0`:
  it re-runs CI, renders all notebooks to HTML and publishes a GitHub Release.

```bash
git tag v1.0.0 && git push origin v1.0.0
```

## Working with Colab

Notebooks saved from Colab push straight to `main`. Before pushing local work, run
`git pull --rebase` so your commits sit on top of the Colab commits.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the branch → PR workflow.
