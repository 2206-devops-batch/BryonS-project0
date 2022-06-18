#!/usr/bin/bash

# call test on changes
python $PWD/lib/test_github_snapshot.py

# if test ok, publish changes.
if [[ $? -eq 0 ]]; then
  git add .
  git commit -m "${@:-'minor change'}"
  git push
fi