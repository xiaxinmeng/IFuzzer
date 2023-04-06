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

def test_var_annot_syntax_errors():
    check_syntax_error(GrammarTests, 'def f: int')
    check_syntax_error(GrammarTests, 'x: int: str')
    check_syntax_error(GrammarTests, 'def f():\n    nonlocal x: int\n')
    check_syntax_error(GrammarTests, '[x, 0]: int\n')
    check_syntax_error(GrammarTests, 'f(): int\n')
    check_syntax_error(GrammarTests, '(x,): int')
    check_syntax_error(GrammarTests, 'def f():\n    (x, y): int = (1, 2)\n')
    check_syntax_error(GrammarTests, 'def f():\n    x: int\n    global x\n')
    check_syntax_error(GrammarTests, 'def f():\n    global x\n    x: int\n')

GrammarTests = test_grammar.GrammarTests()
test_var_annot_syntax_errors()
