import sys 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('test', nargs='*')
result = parser.parse_args(sys.argv[1:])

print("args = %s" % " ".join(sys.argv))
print("result = %s" % result)