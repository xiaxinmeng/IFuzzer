import argparse
import sys

parser = argparse.ArgumentParser(
    allow_abbrev=False
)
parser.add_argument('-a', action='store_true')
parser.add_argument('-b', action='store_true')
parser.add_argument('x', nargs='*')
parser.parse_args('-a -b foo bar'.split())
parser.parse_args('-ab foo bar'.split())