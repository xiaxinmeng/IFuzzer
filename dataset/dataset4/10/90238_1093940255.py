import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--test', action=argparse.BooleanOptionalAction, default=argparse.SUPPRESS, help='Foo')
parser.parse_args()