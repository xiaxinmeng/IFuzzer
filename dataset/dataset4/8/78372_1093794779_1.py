import argparse

parser = argparse.ArgumentParser(description="Automatically process XML")
subparsers = parser.add_subparsers(title='subcommands')

chain_parser = subparsers.add_parser('chain', aliases=['c'], help='Automatically run a chain of transformations')

args = parser.parse_args()