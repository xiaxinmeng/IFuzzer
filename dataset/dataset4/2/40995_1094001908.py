import sys, imp
import pychecker
info = imp.find_module("checker", pychecker.__path__)
sys.argv[0] = info[1]
execfile(info[0])