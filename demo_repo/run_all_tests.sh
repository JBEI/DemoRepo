#!/bin/sh
find . -name "*_test.py" -exec python -m pytest {} \;

# Run integration tests.
