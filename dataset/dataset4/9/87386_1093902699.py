
import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--foo", default="1")
group.add_argument("--bar")
args = parser.parse_args()
print(args)
