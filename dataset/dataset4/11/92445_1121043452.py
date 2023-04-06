
from argparse import ArgumentParser

p = ArgumentParser()
p.add_argument('dessert', nargs='*', choices=('cake', 'pie'))
p.parse_args([])
