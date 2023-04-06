import argparse

parser = argparse.ArgumentParser()
parsers = parser.add_subparsers()
parsers.required = True
parsers.add_parser('foo')
parsers.add_parser('bar')

parser.parse_args()