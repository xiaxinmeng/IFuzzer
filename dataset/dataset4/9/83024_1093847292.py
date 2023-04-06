
import argparse

class CliArgs(object):
    foo: str = 'not touched'


parser = argparse.ArgumentParser()
parser.add_argument('--foo', default='bar')

args = CliArgs()
parser.parse_args(namespace=args)
print(args.foo) # 'not touched'

print(parser.parse_args()) # 'bar'
