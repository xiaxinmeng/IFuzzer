import argparse
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument('-l', '--list', action='store_true', help="show help")
group.add_argument('-u', '--upgrade', action='store_true', help="show help")
parser.parse_args(['--li'])