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

def test_search_star_plus():
    ReTests.assertEqual(re.search('x*', 'axx').span(0), (0, 0))
    ReTests.assertEqual(re.search('x*', 'axx').span(), (0, 0))
    ReTests.assertEqual(re.search('x+', 'axx').span(0), (1, 3))
    ReTests.assertEqual(re.search('x+', 'axx').span(), (1, 3))
    ReTests.assertIsNone(re.search('x', 'aaa'))
    ReTests.assertEqual(re.match('a*', 'xxx').span(0), (0, 0))
    ReTests.assertEqual(re.match('a*', 'xxx').span(), (0, 0))
    ReTests.assertEqual(re.match('x*', 'xxxa').span(0), (0, 3))
    ReTests.assertEqual(re.match('x*', 'xxxa').span(), (0, 3))
    ReTests.assertIsNone(re.match('a+', 'xxx'))

ReTests = test_re.ReTests()
test_search_star_plus()
