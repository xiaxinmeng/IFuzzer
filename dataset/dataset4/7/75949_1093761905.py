import sys
import argparse
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
g2 = parser.add_mutually_exclusive_group()
g2.add_argument("-e", "--eplog", action="store_true")
g2.add_argument("-g", "--quiet", action="store_true")

for i in range(int(sys.argv[1])):
    group.add_argument("z", metavar='Z', type=str, help="the exponent", nargs='?')
    g2.add_argument("z", metavar='Z', type=str, help="the exponent", nargs='?')

parser.parse_args(['-h'])