#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--a-flag')
parser.add_argument('--b-flag')
parser.add_argument('--c-flag')

group = parser.add_mutually_exclusive_group()
group.add_argument('--a-only')
group.add_argument('--b-only')
group.add_argument('positional', nargs='*', default=[])

args = parser.parse_args()