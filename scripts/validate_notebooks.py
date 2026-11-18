"""Fail if any tracked notebook is not a valid Jupyter notebook.

Catches corrupted/empty .ipynb files (e.g. a half-saved file or a bad merge)
before they land on main. Usage: python scripts/validate_notebooks.py [paths...]
"""

from __future__ import annotations

import subprocess
import sys

import nbformat


def tracked_notebooks() -> list[str]:
    out = subprocess.run(
        ["git", "ls-files", "*.ipynb"], capture_output=True, text=True, check=True
    ).stdout
    return [line for line in out.splitlines() if line]


def main(paths: list[str]) -> int:
    paths = paths or tracked_notebooks()
    failures = 0
    for path in paths:
        try:
            nb = nbformat.read(path, as_version=4)
            nbformat.validate(nb)
        except Exception as exc:  # noqa: BLE001 - report every kind of failure
            failures += 1
            print(f"FAIL  {path}: {type(exc).__name__}: {str(exc).splitlines()[0]}")
        else:
            print(f"ok    {path}")
    print(f"\n{len(paths) - failures}/{len(paths)} notebooks valid")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
