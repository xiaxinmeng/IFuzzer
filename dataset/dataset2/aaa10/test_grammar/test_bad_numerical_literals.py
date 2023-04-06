from test.support import check_syntax_error
from test.support.warnings_helper import check_syntax_warning
import inspect
import unittest
import sys
import warnings
from sys import *
import test.ann_module as ann_module
import typing
from collections import ChainMap
from test import ann_module2
import test
from test.support import check_syntax_error
from sys import maxsize
from test.support import check_syntax_error
from test.support.warnings_helper import check_syntax_warning
from test.ann_module3 import f_bad_ann, g_bad_ann, D_bad_ann
import sys
import time, sys
from time import time
from time import time
from sys import path, argv
from sys import path, argv
from sys import path, argv
import sys, time
import test_grammar

def test_bad_numerical_literals():
    check = TokenTests.check_syntax_error
    check('0b12', "invalid digit '2' in binary literal")
    check('0b1_2', "invalid digit '2' in binary literal")
    check('0b2', "invalid digit '2' in binary literal")
    check('0b1_', 'invalid binary literal')
    check('0b', 'invalid binary literal')
    check('0o18', "invalid digit '8' in octal literal")
    check('0o1_8', "invalid digit '8' in octal literal")
    check('0o8', "invalid digit '8' in octal literal")
    check('0o1_', 'invalid octal literal')
    check('0o', 'invalid octal literal')
    check('0x1_', 'invalid hexadecimal literal')
    check('0x', 'invalid hexadecimal literal')
    check('1_', 'invalid decimal literal')
    check('012', 'leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers')
    check('1.2_', 'invalid decimal literal')
    check('1e2_', 'invalid decimal literal')
    check('1e+', 'invalid decimal literal')

TokenTests = test_grammar.TokenTests()
test_bad_numerical_literals()
