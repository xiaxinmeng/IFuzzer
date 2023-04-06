import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display the square of a given number")
parser.add_argument("-v", "--verbosity", action="count",
                    help="increase output verbosity")
parser.add_argument("-f", "--flag", action="store_true")
args = parser.parse_args()

print('args:', args)