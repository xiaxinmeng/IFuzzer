import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
group.add_argument("-x", metavar='X', type=str, help="the base", nargs='?')
group.add_argument("-y", metavar='Y', type=str, help="the exponent", nargs='?')
group.add_argument("z", metavar='Z', type=str, help="the exponent", nargs='?')
group.add_argument("z", metavar='Z', type=str, help="the exponent", nargs='?')
group.add_argument("z", metavar='Z', type=str, help="the exponent", nargs='?')
group.add_argument("z", metavar='Z', type=str, help="the exponent", nargs='?')
group.add_argument("z", metavar='Z', type=str, help="the exponent", nargs='?')
group.add_argument("z", metavar='Z', type=str, help="the exponent", nargs='?')
group.add_argument("z", metavar='Z', type=str, help="the exponent", nargs='?')
#group.add_argument("z", metavar='Z', type=str, help="the exponent", nargs='?')

args = parser.parse_args()