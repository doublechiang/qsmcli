#!/bin/bash
set -e
./test.sh
branch=`git rev-parse --abbrev-ref HEAD`
if [[ $branch != 'master' ]]; then
    # package must pack from master branch
    read -p "git branch is not master, aborting..." input
    exit 1
fi
version=`python3 src/version.py`
git tag $version
git push origin --tags
echo "clean dist/* folder"
rm dist/*
echo "Generate packaged in dist/ folder...."
python3 setup.py sdist bdist_wheel
echo "Uploading to pip repository, providing your username jaingjunyu & password for Pypi"
twine upload dist/*
