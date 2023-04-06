
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('first')
print(parser.parse_args(['-_']))
