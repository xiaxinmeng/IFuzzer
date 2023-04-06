#!/usr/bin/python3 -BEOObbs
# coding=utf-8
import argparse
arguments = argparse.ArgumentParser()
arguments.add_argument('test', action = 'store_true', help = 'Description')
arguments.add_argument('--test', action = 'store_true', help = 'Description')
print(arguments.parse_args())