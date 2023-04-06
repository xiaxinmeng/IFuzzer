
import argparse

arg = argparse.ArgumentParser()
arg.add_argument("opt", action="store_false")

arg.parse_args(["-h"])
