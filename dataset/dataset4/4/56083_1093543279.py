import argparse
parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument ('--a', metavar='a'*76)
parser.add_argument ('--b', metavar="[innerpart]outerpart")
parser.add_argument ('c', metavar='c'*76)
parser.add_argument ('d', metavar="[innerpart2]outerpart2")
args = parser.parse_args()