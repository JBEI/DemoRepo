#!/bin/sh
find . -name "*_test.py" -exec pytest {} \;   
