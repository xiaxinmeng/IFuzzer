
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("pos", nargs="?", default=None)

parser.parse_known_args(["--foo='bar'"])
# (Namespace(pos=None), ['--foo=bar'])
# As expected.

parse.parse_known_args(["--foo='bar baz'"])
# (Namespace(pos="--foo='bar baz'"), [])
# What?!?
