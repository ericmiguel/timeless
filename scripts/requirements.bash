#!/bin/bash

FAILED=false

# requirements
NEW_REQUIREMENTS=$(poetry export -f requirements.txt --without-hashes)

if [ -f requirements.txt ]; then
    echo "requirements.txt exists!"
else
    echo "FAILURE: requirements.txt does not exist!"
    poetry export --format requirements.txt --output requirements.txt --without-hashes
    FAILED=True
fi

REQUIREMENTS=$(cat requirements.txt)

if [ "$NEW_REQUIREMENTS" = "$REQUIREMENTS" ]; then
    echo "requirements.txt is up to date!"
else
    echo "FAILURE: requirements.txt is not up to date!"
    poetry export --format requirements.txt --output requirements.txt --without-hashes
    FAILED=True
fi

if [ "$FAILED" = true ]; then
    exit 1
fi
exit 0