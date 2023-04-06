import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("arg", help="The name is %(prog)s, the sys.argv[0] is " + sys.argv[0])
args = parser.parse_args()