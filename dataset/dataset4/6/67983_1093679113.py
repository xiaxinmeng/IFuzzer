import argparse

p = argparse.ArgumentParser()

g1 = p.add_mutually_exclusive_group(required=False)
g1.add_argument("-a")
g1.add_argument("-b")

g2 = p.add_mutually_exclusive_group(required=False)
g2.add_argument("-c")
g2.add_argument("-d")

p.parse_args()