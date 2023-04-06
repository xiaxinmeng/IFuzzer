#!/usr/bin/env python
import argparse

print("\n\narg=foo, nargs=+")
parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('foo', nargs='+', help='foos', default=['foo1', 'foo2'])
parser.print_help()

print("\n\narg=foo, nargs=*")
parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('foo', nargs='*', help='foos', default=['foo1', 'foo2'])
parser.print_help()

print("\n\narg=--foo, nargs=+")
parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--foo', nargs='+', help='foos', default=['foo1', 'foo2'])
parser.print_help()

print("\n\narg=--foo, nargs=*")
parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--foo', nargs='*', help='foos', default=['foo1', 'foo2'])
parser.print_help()