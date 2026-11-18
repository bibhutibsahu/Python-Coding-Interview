# Contributing

## Workflow

1. **Sync:** `git switch main && git pull --rebase`
2. **Branch:** `git switch -c feat/<short-name>` (or `fix/…`, `chore/…`, `docs/…`)
3. **Work:** add or edit notebooks and scripts. The pre-commit hooks run on every commit.
4. **Check:** `make ci`
5. **Commit** using [Conventional Commits](https://www.conventionalcommits.org/):
   - `feat: add two-sum solution`
   - `fix: correct pareto crossing month`
   - `ci: run notebooks on python 3.12`
6. **Push and open a PR:** `git push -u origin HEAD`, then open a pull request on GitHub.
   CI must be green before merging. Squash-merge to keep `main` history clean.

## Notebooks

- A notebook only joins `ci/notebooks-to-execute.txt` once it runs from a fresh kernel:
  no `/content/drive/...` paths, no `input()`, and every import listed in `requirements.txt`.
- Load data with relative paths (`pd.read_csv("train.csv")`) so the notebook works in CI and locally.

## Dependencies

Add runtime libraries to `requirements.txt` and tooling to `requirements-dev.txt`, both pinned
(`package==x.y.z`). Dependabot proposes upgrades every week.

## Releasing

Update the `version` in `pyproject.toml`, merge to `main`, then:

```bash
git tag vX.Y.Z && git push origin vX.Y.Z
```
