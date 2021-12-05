#!/bin/bash

### Check if input has been supplied
if [ -z "$1" ]
  then
    echo "Error! No argument supplied"
    exit 1
fi

### Check if day already exists
if test -f "${1}.py"
  then
    echo 'Error! File already exists'
    exit 1
fi

### Set up solution file
cp templates/day_template.py ./${1}.py
sed -i 's/dayXX/'"${1}"'/g' ${1}.py

### Set up test file
cp templates/day_test_template.py ./tests/${1}_test.py
sed -i 's/dayXX/'"${1}"'/g' tests/${1}_test.py

### Set up data files
mkdir data/${1}
touch data/${1}/realdata
touch data/${1}/testdata

echo 'OK to go!'
