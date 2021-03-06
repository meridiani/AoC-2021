# AoC-2021
Another advent of code...

You can find the challenges here: [Advent of Code 2021](https://adventofcode.com/2021)

# My personal goals for this year

🤷‍♀️ beat last year's record of eight days  
✔️ use python virtualenv  
✔️ write some unit tests  

# Using this repo

## Virtualenv
I'm using virtualenv to manage python dependencies.

To set up virtualenv on a linux machine:

```
cd working_directory
python3.8 -m venv virtualenv
```

Then to activate your session:

`source virtualenv/bin/activate`

And then deactivate when you are done:

`deactivate`

## Set up a new day
A bash script has been provided to set up a new day like so:

```
./new_day.sh day09
```

## Solution code

Each days data is in `data/day{number}/` and is split into testdata and realdata

The solutions are currently in one file per day e.g. day01.py

To run:
```
source virtualenv/bin/activate
./day01.py
```

Useful shared functions go in utils.py

# Unit testing
This is a work in progress

Each module has a corresponding unit test file in `tests`

To run:

```
python -m unittest tests/utils_test.py 
```
