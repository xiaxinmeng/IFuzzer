import argparse
parser = argparse.ArgumentParser()
parser.add_argument("inputfiles", metavar = 'input_file(s)', nargs = "+", help = 'one or more input files')

args = parser.parse_args()