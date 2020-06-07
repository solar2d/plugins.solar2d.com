#!/usr/bin/env bash
set -e
mkdir -p docs
./generate.py plugins/*.json > docs/plugins.json
