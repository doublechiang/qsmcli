#!/bin/bash
set -e
./test.sh
branch=`git rev-parse --abbrev-ref HEAD`
if [[ $branch != 'master' ]]; then
    read -p "git branch is not master, hit ctrl-c to break"
fi
python3 setup.py sdist bdist_wheel
echo "Generate packaged in dist/ folder...."
