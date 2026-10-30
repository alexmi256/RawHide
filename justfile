# Task runner for stegodng. Install just from https://github.com/casey/just,
# then run `just --list`. Needs the dev dependencies:
# `.venv/bin/pip install -r requirements-dev.txt`.

# Python interpreter for dev tasks. Defaults to the repo venv; override for a
# different environment with `PYTHON=/path/to/venv/bin/python just ...`.
# Recipes fail loudly when this is missing instead of silently using a system
# Python that lacks the dev dependencies.
python := env_var_or_default("PYTHON", ".venv/bin/python")

# List available recipes.
default:
    @just --list

# Prepare the dev environment. A linked git worktree does not get the
# git-ignored .venv; link the main checkout's venv instead of duplicating it.
setup:
    #!/usr/bin/env bash
    set -euo pipefail
    if [ -x .venv/bin/python ]; then
        echo ".venv already present"
        exit 0
    fi
    if [ -e .venv ] || [ -L .venv ]; then
        echo "error: .venv exists but is not a usable environment" >&2
        exit 1
    fi
    common_dir="$(git rev-parse --path-format=absolute --git-common-dir)"
    main_root="$(dirname "$common_dir")"
    if [ -x "$main_root/.venv/bin/python" ]; then
        ln -s "$main_root/.venv" .venv
        echo "linked .venv -> $main_root/.venv"
    else
        python3 -m venv .venv
        .venv/bin/python -m pip install -r requirements-dev.txt
    fi

[private]
_check-python:
    @command -v {{ python }} >/dev/null 2>&1 || { echo "error: '{{ python }}' not found." >&2; echo "Run 'just setup' or set PYTHON=/path/to/venv/bin/python." >&2; exit 1; }

# Run the test suite (extra args are forwarded to pytest, e.g. `just test -k roundtrip`).
test *args="": _check-python
    {{ python }} -m pytest tests/ -q {{ args }}

# Lint the shipped package (error-level ruff rules; see [tool.ruff] in pyproject.toml).
lint: _check-python
    {{ python }} -m ruff check stegodng stego_dng.py

# Type-check the shipped package with Pyrefly (see [tool.pyrefly] in
# pyproject.toml; extra args are forwarded, e.g. `just typecheck --summarize-errors`).
typecheck *args="": _check-python
    {{ python }} -m pyrefly check {{ args }}

# Build an sdist + wheel into dist/ and verify the metadata renders.
build: _check-python
    rm -rf dist/ build/
    {{ python }} -m build
    {{ python }} -m twine check dist/*

# Upload dist/* to TestPyPI. Auth via TWINE_USERNAME=__token__ and
# TWINE_PASSWORD=<testpypi-token>, or a ~/.pypirc entry. Verifies on
# https://test.pypi.org/project/stegodng/ before a real release.
publish-test: build
    {{ python }} -m twine upload --repository testpypi dist/*

# Upload dist/* to PyPI. Auth via TWINE_USERNAME=__token__ and
# TWINE_PASSWORD=<pypi-token>, or a ~/.pypirc entry.
publish: build
    {{ python }} -m twine upload dist/*

# Remove build artifacts.
clean:
    rm -rf dist/ build/ *.egg-info/ stegodng.egg-info/
