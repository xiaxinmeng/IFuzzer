#!/usr/bin/python3 -BEOObbs
# coding=utf-8
import argparse
arguments = argparse.ArgumentParser()
arguments.add_argument('-t', '--test1', action = 'store_true', help = 'Description1')
arguments.add_argument('--test2', action = 'store_true', help = 'Description2')
arguments.add_argument('-u', '--test3', choices = ['choice1', 'choice2'], help = 'Description3', nargs = '+')
arguments.parse_args()