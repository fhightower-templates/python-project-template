#!/usr/bin/env bash

set -euxo pipefail

echo "Running linters and formatters..."

isort {{cookiecutter.project_slug}}/ tests/

black {{cookiecutter.project_slug}}/ tests/

mypy {{cookiecutter.project_slug}}/ tests/

pylint {{cookiecutter.project_slug}}/*.py

flake8 {{cookiecutter.project_slug}}/ tests/

bandit -r {{cookiecutter.project_slug}}/

# we run black again at the end to undo any odd changes made by any of the linters above
black {{cookiecutter.project_slug}}/ tests/
