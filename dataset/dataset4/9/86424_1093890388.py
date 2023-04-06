import argparse

ap = argparse.ArgumentParser(allow_abbrev=False)
ap.add_argument('-c', '--choices', choices=['a', 'b', 'c'])
ap.parse_args()