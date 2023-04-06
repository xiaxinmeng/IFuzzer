import argparse
foo = int(1e3) # Works: foo = 1000
parser = argparse.ArgumentParser()
parser.add_argument( "--foo", type=int )
parser.parse_args( ["--foo=1e3"] )
# error: argument --foo: invalid int value: '1e3'