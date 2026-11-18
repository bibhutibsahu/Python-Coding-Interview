# Common developer commands. Run `make help` to list them.
VENV   := .venv
PY     := $(VENV)/bin/python
BIN    := $(VENV)/bin
NOTEBOOKS := $(shell grep -vE '^\s*(\#|$$)' ci/notebooks-to-execute.txt)

.DEFAULT_GOAL := help
.PHONY: help setup lint format test notebooks validate ci clean

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN{FS=":.*?## "}{printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2}'

$(VENV):
	python3 -m venv $(VENV)

setup: $(VENV) ## Create .venv, install deps, install git hooks
	$(PY) -m pip install --upgrade pip
	$(PY) -m pip install -r requirements-dev.txt
	$(BIN)/pre-commit install

lint: ## Lint + format check (same as CI)
	$(BIN)/ruff check .
	$(BIN)/ruff format --check .

format: ## Auto-fix lint issues and format code
	$(BIN)/ruff check --fix .
	$(BIN)/ruff format .

validate: ## Check every notebook is valid JSON/nbformat
	$(PY) scripts/validate_notebooks.py

test: ## Run unit tests
	$(BIN)/pytest

notebooks: ## Execute the curated notebooks
	MPLBACKEND=Agg $(BIN)/pytest --nbmake --nbmake-timeout=300 -p no:cacheprovider $(NOTEBOOKS)

ci: lint validate test notebooks ## Run the full CI pipeline locally

clean: ## Remove caches and build output
	rm -rf .pytest_cache .ruff_cache dist build **/__pycache__
