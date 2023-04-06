import argparse

parser = argparse.ArgumentParser()
subp = parser.add_subparsers()
subp.add_parser('test')
subp.required = True
parser.parse_args()