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

def test_floats():
    x = 3.14
    x = 314.0
    x = 0.314
    x = 0.314
    x = 300000000000000.0
    x = 300000000000000.0
    x = 3e-14
    x = 300000000000000.0
    x = 300000000000000.0
    x = 30000000000000.0
    x = 31000.0

TokenTests = test_grammar.TokenTests()
test_floats()
