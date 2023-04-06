import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--list-arg', nargs='+', default=[])
parser.parse_known_args(['--list-arg', 'a', '--text-arg=hello world'])