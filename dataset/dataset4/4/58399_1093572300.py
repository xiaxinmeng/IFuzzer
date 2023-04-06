from argparse import ArgumentParser, SUPPRESS, REMAINDER
import sys
print( sys.version )
parser = ArgumentParser()
parser.add_argument('--foo', dest='foo')
parser.add_argument('--bar', dest='bar')
parser.add_argument('baz', nargs='*')
print( parser.parse_args('a b --foo x --bar 1 c d'.split()))
# expected:  Namespace(bar='1', baz=['a', 'b', 'c', 'd'], foo='x')
# actual: error: unrecognized arguments: c d