import argparse

epilog = """\
Example usage:
  %(prog)s option1 option2
"""
parser = argparse.ArgumentParser(
    formatter_class=argparse.RawTextHelpFormatter,
    epilog=epilog)
parser.parse_args()