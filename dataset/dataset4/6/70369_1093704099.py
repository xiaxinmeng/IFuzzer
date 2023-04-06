import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename')
parser.add_argument('-L', metavar='integer', type=int, nargs='+')
args = parser.parse_args()
print(args)  # see what we got