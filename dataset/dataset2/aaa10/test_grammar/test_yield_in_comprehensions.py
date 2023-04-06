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

def test_yield_in_comprehensions():

    def g():
        [x for x in [(yield 1)]]

    def g():
        [x for x in [(yield from ())]]
    check = GrammarTests.check_syntax_error
    check('def g(): [(yield x) for x in ()]', "'yield' inside list comprehension")
    check('def g(): [x for x in () if not (yield x)]', "'yield' inside list comprehension")
    check('def g(): [y for x in () for y in [(yield x)]]', "'yield' inside list comprehension")
    check('def g(): {(yield x) for x in ()}', "'yield' inside set comprehension")
    check('def g(): {(yield x): x for x in ()}', "'yield' inside dict comprehension")
    check('def g(): {x: (yield x) for x in ()}', "'yield' inside dict comprehension")
    check('def g(): ((yield x) for x in ())', "'yield' inside generator expression")
    check('def g(): [(yield from x) for x in ()]', "'yield' inside list comprehension")
    check('class C: [(yield x) for x in ()]', "'yield' inside list comprehension")
    check('[(yield x) for x in ()]', "'yield' inside list comprehension")

GrammarTests = test_grammar.GrammarTests()
test_yield_in_comprehensions()
