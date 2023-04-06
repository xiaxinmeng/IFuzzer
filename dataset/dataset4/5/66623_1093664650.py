import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--known-optional-arg", "-k", action="store_true")
parser.add_argument("known_positional", action="store", type=str)
parser.parse_known_args(["--known-optional-arg", "--unknown-optional-arg=with spaces", "known positional arg"])
parser.parse_known_args(["--known-optional-arg", "--unknown-optional-arg=without_spaces", "known positional arg"])