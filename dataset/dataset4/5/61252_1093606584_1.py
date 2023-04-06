print('What we want to do is have a subparser that, in the case of one particular selection, forwards all following arguments to another tool.')
print('script.py --foo B cmdname --arg1 XX ZZ --foobar should dispatch to cmdname --arg1 XX ZZ --foobar.')
parser = argparse.ArgumentParser()
parser.add_argument('--foo')
subparsers = parser.add_subparsers(dest='command')
commandParser = subparsers.add_parser('cmdname')
commandParser.add_argument('cmdname_args', nargs=argparse.REMAINDER)
parser.parse_args('--foo B cmdname --arg1 XX ZZ --foobar'.split())
# error: unrecognized arguments: --arg1