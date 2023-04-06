from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('--foo', action='store', help='%bar')

args = parser.parse_args('-h'.split())