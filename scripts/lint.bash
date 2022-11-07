#!/bin/bash

set -e
set -x

mypy timeless --enable-incomplete-features
flake8 timeless tests
black timeless tests --check
isort timeless tests docs_src scripts --check-only
pydocstyle timeless
