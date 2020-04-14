#!/usr/bin/env bash
set -e
git submodule --quiet foreach 'git fetch --quiet --depth=1 origin +refs/tags/*:refs/tags/* || echo error with $sm_path'
git submodule --quiet foreach 'git describe --tags --abbrev=0 > RELEASE || echo Release error with $sm_path'
mkdir -p html
./generate.py plugins > html/plugins.json
