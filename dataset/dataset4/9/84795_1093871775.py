from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--clear-magic", action="store_true")
print(parser.parse_args(["--clear"]))

parser.add_argument("--clear", action="store_true")
print(parser.parse_args(["--clear"]))