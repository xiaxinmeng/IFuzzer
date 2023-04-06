import argparse
foo = int(1e3) # Works: foo = 1000
parser = argparse.ArgumentParser()
parser.add_argument( "--foo", type=lambda x: int(float(x)))
parser.parse_args( ["--foo=1e3"] )