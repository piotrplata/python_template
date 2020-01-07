#!/bin/bash

GEMFURY_URL=$GEMFURY_PUSH_URL

set -e
python setup.py sdist bdist_wheel

for X in $(ls dist)
    do
        curl -F package=@"dist/$X" "$GEMFURY_URL"
    done