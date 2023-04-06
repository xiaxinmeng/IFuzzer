import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '--foo',
    action='append',
    default=['bar1', 'bar2']
)
args = parser.parse_args()