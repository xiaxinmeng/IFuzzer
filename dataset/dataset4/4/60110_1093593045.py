import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test", dest="test", type=str,
    default=[], action='append')

args = parser.parse_args()