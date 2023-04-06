import argparse
from getpass import getuser
parser = argparse.ArgumentParser(description='An argparse example.')
parser.add_argument('name', nargs='?', default=getuser(),  # wrap
                    help='The name of someone to greet.')
parser.add_argument('--verbose', '-v', action='count')
args = parser.parse_args()  # new
args.verbose = 0 if args.verbose is None else args.verbose
greeting = (["Hi", "Hello", "Greetings! its very nice to meet you"] #wrap
            [args.verbose % 3])
print(f'{greeting}, {args.name}')