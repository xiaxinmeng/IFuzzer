
# a.py

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--a", required=True)
parser.add_argument("--b", required=True)
parser.parse_args()
