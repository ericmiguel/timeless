#!/bin/bash -e

set -x
autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place docs_src timeless tests scripts --exclude=__init__.py
black timeless tests docs_src scripts
isort timeless tests docs_src scripts