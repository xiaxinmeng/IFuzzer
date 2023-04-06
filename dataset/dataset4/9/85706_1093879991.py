import argparse
parser = argparse.ArgumentParser(allow_abbrev=True)
parser.add_argument('-o', type=str, required=True, dest="bla", help="bla")
known_args, rest_of_args = parser.parse_known_args(["-o", "test1", "-object_lto", "test2"])
print(rest_of_args)