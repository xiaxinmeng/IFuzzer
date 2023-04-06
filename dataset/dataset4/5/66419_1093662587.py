import argparse
parser = argparse.ArgumentParser(prog="PROG")
parser.add_argument("--args", nargs=argparse.REMAINDER)
args = parser.parse_args("--args cmd --arg1 XX ZZ".split())
assert args.args == ["cmd", "--arg1", "XX", "ZZ"]