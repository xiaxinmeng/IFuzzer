import argparse
import sys

parser = argparse.ArgumentParser(prog=sys.argv[0], add_help=False)
parser.add_argument('-a', action='store_true')
parser.add_argument('-b', action='store_true')
parser.add_argument('-c', action='store_true')
parsed_args, unknown_args = parser.parse_known_args(sys.argv[1:])
print(parsed_args)
print(unknown_args)