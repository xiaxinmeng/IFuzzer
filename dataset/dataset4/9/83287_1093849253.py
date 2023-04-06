import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--include-ssl', action='store_true')
namespace = parser.parse_args()