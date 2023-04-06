#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument('positional', nargs='*', default=[])
group.add_argument('--flag')

args = parser.parse_args()