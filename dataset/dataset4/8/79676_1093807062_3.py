import argparse
parser = argparse.ArgumentParser()
parser.add_argument('foo', nargs=1,default=['none'])
parser.add_argument('bar', nargs=argparse.REMAINDER,default=['nothing'])
#parser.add_argument('baz', nargs='*', default=['nada'])
parser.parse_args('a'.split())