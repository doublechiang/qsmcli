#!/bin/bash
set -e
./test.sh
branch=`git rev-parse --abbrev-ref HEAD`
if [[ $branch != 'master' ]]; then
    read -p "git branch is not master, press Y if you really want to continue.." input
    if [[ $input != 'Y' ]]; then
        exit 1
    fi
fi
echo "clean dist/* folder"
rm dist/*
echo "Generate packaged in dist/ folder...."
python3 setup.py sdist bdist_wheel
twine upload dist/*
