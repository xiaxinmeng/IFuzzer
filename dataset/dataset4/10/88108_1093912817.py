
from argparse import ArgumentParser, RawDescriptionHelpFormatter

parser = ArgumentParser(
  description='A simple templating system.',
  epilog='Use `-\' as a file name to indicate standard input or output.',
  formatter_class=RawDescriptionHelpFormatter,
)
parser.add_argument(
  '--verbose',
  help='show on standard error the path being built,\nand the names of files built, included and pasted'
)
args = parser.parse_args()
