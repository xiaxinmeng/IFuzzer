import argparse
# based on Vajrasky Kok's script in https://bugs.python.org/issue11874
parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('--nil', metavar='', required=True)
parser.add_argument('--a', metavar='a' * 165)
parser.parse_args()