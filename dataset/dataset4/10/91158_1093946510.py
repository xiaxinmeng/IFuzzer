import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--utc", choices=["-1:00"])
args = parser.parse_args()