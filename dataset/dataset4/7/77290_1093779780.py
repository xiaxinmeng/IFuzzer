import argparse
parser = argparse.ArgumentParser(prog='PROG')
subparsers = parser.add_subparsers(required=True)
parser_a = subparsers.add_parser('a')
parser_b = subparsers.add_parser('b')
parser.parse_args([])