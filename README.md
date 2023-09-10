# Scrabble

Scrabble is a simplified Scrabble game that generates a leaderboard based on the ```wordlist.txt``` that is considered
valid
and the input letters (if any).
It outputs a text with all the highest words ordered in descending order with the highest scoring first. If several
words have the same score they are ordered alphabetically in the ascending order.

## Installation

The repository is ran on a Linux system with the below configurations

```
Basic info
OS                       : Debian GNU/Linux 11 (bullseye)
OS version               : 11
OS Config agent version  : 20230330.00-g1
Image                    : debian-11-bullseye-v20230411
Python                   : Python 3.9.2
python3-venv             : 3.9.2-3
```

Use setup the virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Usage

To run and generate results,

```bash
python3 main.py -i files/input.txt -o files/output.txt -letters
```

If no command-line flags are used, output file will be ```files/output.txt``` in the repository folder and we will
run the function ```build_leaderboard_for_word_list ```instead of ```build_leaderboard_for_letters```

Arguments available for main.py

```
-i, --input     : input file name (default to files/input.txt but unused if -l/--letters provided)
-o, --output    : output file name (default to files/output.txt)
-l, --letters   : If argument not provided, we will be running 𝙗𝙪𝙞𝙡𝙙_𝙡𝙚𝙖𝙙𝙚𝙧𝙗𝙤𝙖𝙧𝙙_𝙛𝙤𝙧_𝙬𝙤𝙧𝙙_𝙡𝙞𝙨𝙩 instead of 𝙗𝙪𝙞𝙡𝙙_𝙡𝙚𝙖𝙙𝙚𝙧𝙗𝙤𝙖𝙧𝙙_𝙛𝙤𝙧_𝙡𝙚𝙩𝙩𝙚𝙧𝙨
```

## Testing and Coverage

To run and generate testing results and coverage report (both console and HTML),

```bash
python3 run_tests.py -v
```

If no command-line flags are used, pytest is set as high verbosity level

Arguments available for run_tests.py

```
-q, --quiet   : Low verbosity
-v, --verbose : High verbosity
```

Below we see the coverage of testing done

```
Name                                                                 Stmts   Miss  Cover
----------------------------------------------------------------------------------------
/home/yjthay/unladen_swallow/highscoringwords.py                        44      0   100%
__init__.py                                                              0      0   100%
test_highscoringwords.py                                                32      0   100%
----------------------------------------------------------------------------------------
TOTAL                                                                   76      0   100%
```

The below folder shows the generated HTML reports after run_tests.py has been executed and provides a view of specific
lines that were not ran during testing.

```bash
(venv) thayyeejie@unladen_swallow:/home/yjthay/unladen_swallow/test/htmlcov$ ls
__init___py.html                coverage_html.js            d_66f8bef7029fb3db_highscoringwords_py.html  
favicon_32.png                  index.html                  keybd_closed.png  
keybd_open.png                  status.json                 style.css
test_highscoringwords_py.html
```

## Additional discussions/ expansion to consider

