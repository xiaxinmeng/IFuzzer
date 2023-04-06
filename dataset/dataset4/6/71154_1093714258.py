#! /usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(allow_abbrev=True)
parser.add_argument('-v', '--verbose', action='count')
print(parser.parse_args(['-vv']))

parser = argparse.ArgumentParser(allow_abbrev=False)
parser.add_argument('-v', '--verbose', action='count')
print(parser.parse_args(['-vv']))