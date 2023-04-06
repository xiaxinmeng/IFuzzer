#!/usr/bin/env python3.6 
errfile = 'test_err.txt'

import sys
errorlog = open(errfile, 'w')
sys.stderr = errorlog