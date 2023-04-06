import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--ng", action="store_true")
parser.add_argument("--INP")
print(parser.parse_args())