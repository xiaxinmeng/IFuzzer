import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', dest='tf', action='store_true')

subs = parser.add_subparsers()

sub = subs.add_parser('cmd')
sub.add_argument('-f', dest='cf', action='store_true')

parser.add_argument('arg')

args = parser.parse_args()
print(args)