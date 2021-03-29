#!/bin/sh
set -e -x

# Run all tests and calculate coverage.
coverage run --source=. -m pytest
coverage html
coverage report
