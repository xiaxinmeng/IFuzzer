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

def test_re_subn():
    ReTests.assertEqual(re.subn('(?i)b+', 'x', 'bbbb BBBB'), ('x x', 2))
    ReTests.assertEqual(re.subn('b+', 'x', 'bbbb BBBB'), ('x BBBB', 1))
    ReTests.assertEqual(re.subn('b+', 'x', 'xyz'), ('xyz', 0))
    ReTests.assertEqual(re.subn('b*', 'x', 'xyz'), ('xxxyxzx', 4))
    ReTests.assertEqual(re.subn('b*', 'x', 'xyz', 2), ('xxxyz', 2))
    ReTests.assertEqual(re.subn('b*', 'x', 'xyz', count=2), ('xxxyz', 2))

ReTests = test_re.ReTests()
test_re_subn()
