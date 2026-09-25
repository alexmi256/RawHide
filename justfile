# Task runner for stegodng. Install just from https://github.com/casey/just,
# then run `just --list`. Needs the dev dependencies:
# `.venv/bin/pip install -r requirements-dev.txt`.

# Prefer the repo venv (see AGENTS.md); fall back to system python3.
python := if path_exists(".venv/bin/python") != "" { ".venv/bin/python" } else { "python3" }

# List available recipes.
default:
    @just --list

# Run the test suite (extra args are forwarded to pytest, e.g. `just test -k roundtrip`).
test *args="":
    {{ python }} -m pytest tests/ -q {{ args }}

# Lint the shipped package (error-level ruff rules; see [tool.ruff] in pyproject.toml).
lint:
    {{ python }} -m ruff check stegodng stego_dng.py

# Type-check the shipped package with Pyrefly (see [tool.pyrefly] in
# pyproject.toml; extra args are forwarded, e.g. `just typecheck --summarize-errors`).
typecheck *args="":
    {{ python }} -m pyrefly check {{ args }}

# Build an sdist + wheel into dist/ and verify the metadata renders.
build:
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
