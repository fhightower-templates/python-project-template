#!/usr/bin/env bash

set -euxo pipefail

echo "Running linters and formatters..."

isort d8s_dates/ tests/

black d8s_dates/ tests/

mypy d8s_dates/ tests/

pylint d8s_dates/*.py

flake8 d8s_dates/ tests/

bandit -r d8s_dates/

# we run black again at the end to undo any odd changes made by any of the linters above
black d8s_dates/ tests/
