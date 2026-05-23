#!/bin/bash

find . -type f \
    -not -path "./.git/*" \
    -not -path "./README.md" \
    -not -path "./count_solutions.*" \
    -not -path "./.gitignore" \
    -not -path "./LICENSE" \
    | wc -l
