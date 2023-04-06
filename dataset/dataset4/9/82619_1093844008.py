import argparse
ap = argparse.ArgumentParser()
ap.add_argument("arg", nargs="*")
ap.parse_args()