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

def test_matrix_mul():

    class M:

        def __matmul__(GrammarTests, o):
            return 4

        def __imatmul__(GrammarTests, o):
            GrammarTests.other = o
            return GrammarTests
    m = M()
    GrammarTests.assertEqual(m @ m, 4)
    m @= 42
    GrammarTests.assertEqual(m.other, 42)

GrammarTests = test_grammar.GrammarTests()
test_matrix_mul()
