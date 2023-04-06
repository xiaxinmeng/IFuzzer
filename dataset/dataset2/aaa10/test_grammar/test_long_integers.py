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

def test_long_integers():
    x = 0
    x = 18446744073709551615
    x = 18446744073709551615
    x = 2251799813685247
    x = 2251799813685247
    x = 123456789012345678901234567890
    x = 295147905179352825856
    x = 590295810358705651711

TokenTests = test_grammar.TokenTests()
test_long_integers()
