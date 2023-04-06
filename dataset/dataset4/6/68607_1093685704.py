import argparse

parser = argparse.ArgumentParser()
parser.add_argument('x', action='append')
parser.add_argument('x', action='append_const', const=42, metavar='foo')
parser.add_argument('x', action='append_const', const=43, metavar='bar')
parser.add_argument('-x', action='append_const', const=44)

args = parser.parse_args()
print(args)