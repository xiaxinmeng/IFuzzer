from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument('foo', choices=['foo'], nargs='*')
args = parser.parse_args([])  # <-- fails, error message below
assert args.foo == []
# usage: args.py [-h] [{foo} [{foo} ...]]
# args.py: error: argument foo: invalid choice: [] (choose from 'foo')