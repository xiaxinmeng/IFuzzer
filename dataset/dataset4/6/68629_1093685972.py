import argparse

parser = argparse.ArgumentParser()
parser.add_argument('foo', choices=[])

args = parser.parse_args()
print(args)