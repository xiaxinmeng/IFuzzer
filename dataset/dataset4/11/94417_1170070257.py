
import argparse
import sys

print(f"argv = {sys.argv}")

parser = argparse.ArgumentParser(description='Print value.')
parser.add_argument('--valueA', type=str, dest="valueA")
parser.add_argument('--valueB', type=str, dest="valueB")

args = parser.parse_args()
print(f"Passed --valueA = '{args.valueA}'")
print(f"Passed --valueB = '{args.valueB}'")
