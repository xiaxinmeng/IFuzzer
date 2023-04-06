import argparse

global_options = argparse.ArgumentParser(add_help=False)
global_options.add_argument('--summary', action='store_true', help='summarize information')
global_options.add_argument('--verbose', action='store_true', help='tell us more')

output_format = global_options.add_argument_group("Output format", "ways to foo")
styles = output_format.add_mutually_exclusive_group()
styles.add_argument('--plain', dest='style')
styles.add_argument('--green', dest='style')
styles.add_argument('--blue', dest='style')

parser = argparse.ArgumentParser()
commands = parser.add_subparsers()
hit = commands.add_parser('hit', parents=[global_options])
miss = commands.add_parser('miss', parents=[global_options])

print(parser.parse_args(['hit', '-h']))