
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
subparsers = parser.add_subparsers()

# create the parser for the "a" command
parser_a = subparsers.add_parser('a', help='a help', description='test me')
parser_a.add_argument('bar', type=int, help='bar help')

print(parser.parse_args())
