import argparse
ap = argparse.ArgumentParser()
ap.add_argument("--option", action="store_true")
ap.add_argument("arg_1")
ap.add_argument("arg_2", nargs="?")
print("test 1:", ap.parse_args(["abc", "mmm", "--option"]))
print("test 2:", ap.parse_args(["abc", "--option", "mmm"]))