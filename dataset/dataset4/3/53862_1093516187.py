import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--foo')

if len(sys.argv) == 1:
    parser.print_help()  
else:
    print(parser.parse_args())