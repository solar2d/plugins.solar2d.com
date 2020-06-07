#!/usr/bin/env bash
set -e
mkdir -p html
./generate.py plugins/*.json > html/plugins.json
