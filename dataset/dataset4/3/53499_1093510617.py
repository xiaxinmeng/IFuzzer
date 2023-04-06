from argparse import ArgumentParser
parser = ArgumentParser(prog='test')
subparsers = parser.add_subparsers()
subparser = subparsers.add_parser("foo", help="run foo")
parser.parse_args()