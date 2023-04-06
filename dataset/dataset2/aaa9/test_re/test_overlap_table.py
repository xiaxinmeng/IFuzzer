from test.support import gc_collect, bigmemtest, _2G, cpython_only, captured_stdout
import locale
import re
import sre_compile
import string
import unittest
import warnings
from re import Scanner
from weakref import proxy
from sre_constants import MAXGROUPS
import _sre
import pickle
from re import _compile
import copy
import array
import _sre
from _sre import MAXREPEAT
from test.re_tests import benchmarks
from test.re_tests import tests, FAIL, SYNTAX_ERROR
import test_re

def test_overlap_table():
    f = sre_compile._generate_overlap_table
    ImplementationTest.assertEqual(f(''), [])
    ImplementationTest.assertEqual(f('a'), [0])
    ImplementationTest.assertEqual(f('abcd'), [0, 0, 0, 0])
    ImplementationTest.assertEqual(f('aaaa'), [0, 1, 2, 3])
    ImplementationTest.assertEqual(f('ababba'), [0, 0, 1, 2, 0, 1])
    ImplementationTest.assertEqual(f('abcabdac'), [0, 0, 0, 1, 2, 0, 1, 0])

ImplementationTest = test_re.ImplementationTest()
test_overlap_table()
