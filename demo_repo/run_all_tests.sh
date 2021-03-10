#!/bin/sh
set -e -x

# Run all of the python tests.
find . -name "*_test.py" -exec python -m pytest {} \;

# Calculate coverage.
coverage run --source=. -m pytest
find . -name "*.py" -exec python -m pytest {} \;
coverage html
coverage report
