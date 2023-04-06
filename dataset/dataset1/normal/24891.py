import argparse

parser = argparse.ArgumentParser(description="Test python script")
parser.add_argument('-o', type=argparse.FileType('a'), metavar='outfile')
args = parser.parse_args()

outfile = args.o

print("It Worked!", file=outfile)
