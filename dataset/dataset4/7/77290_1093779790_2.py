import argparse

parser = argparse.ArgumentParser()
subp = parser.add_subparsers(dest='cmd')
subp.add_parser('test')
subp.required = True
parser.parse_args()