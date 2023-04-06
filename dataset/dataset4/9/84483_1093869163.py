import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--boolean", type=bool)
parsed_args = parser.parse_args(["--boolean=''"])