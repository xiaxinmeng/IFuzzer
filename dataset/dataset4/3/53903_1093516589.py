import argparse

parser = argparse.ArgumentParser(
    description = 'Do something'
)
parser.add_argument('--reqarg', '-r', help = 'This is required', required = True)
parser.add_argument('--optarg','-o', help = "This is optional", required = False)
args = parser.parse_args()