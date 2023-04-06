import argparse
ap=argparse.ArgumentParser()
ap.add_argument("--a-b", "--ab")
v1=ap.parse_args(["--ab", "xx"])
print(v1)
# v1==Namespace(a_b='xx')
v2=ap.parse_args(["--a", "xx"])
# v2 should be equal to v1 but instead it raises an error, in spite that --a-b and --ab are aliases