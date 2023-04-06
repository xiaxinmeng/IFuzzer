import argparse

parser = argparse.ArgumentParser()
parser.add_argument('echo', type=argparse.FileType)
args = parser.parse_args()
print(args.echo)