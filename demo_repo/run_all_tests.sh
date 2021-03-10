#!/bin/sh
# Run all of the python tests.
find . -name "*_test.py" -exec python -m pytest {} \;
