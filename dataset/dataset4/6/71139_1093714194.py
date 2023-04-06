import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
parser.parse_args(['-h'])