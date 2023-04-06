import argparse

def parse(args, **kwargs):
    parser = argparse.ArgumentParser()
    parser.add_argument('foo', **kwargs)
    ns = parser.parse_args(args)
    print(repr(ns.foo))

parse([], nargs='?')                # None
parse([], nargs='*')                # []    <--
parse([], nargs='*', default=None)  # []    <--
parse([], nargs='*', default=False) # False
parse([], nargs='*', default=0)     # 0