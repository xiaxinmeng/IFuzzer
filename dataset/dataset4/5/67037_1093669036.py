parser = argparse.ArgumentParser('test')
subparsers = parser.add_subparsers()
parser_foo = subparsers.add_parser('foo', help='This is help for foo')
parser_bar = subparsers.add_parser('bar', help=argparse.SUPPRESS)

parser.parse_args(['-h'])