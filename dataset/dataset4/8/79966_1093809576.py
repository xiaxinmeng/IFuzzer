import argparse

p = argparse.ArgumentParser()
p.add_argument('--foo', nargs=None)
args = p.parse_args()