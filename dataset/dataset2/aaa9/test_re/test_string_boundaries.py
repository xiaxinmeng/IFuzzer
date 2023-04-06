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

def test_string_boundaries():
    ReTests.assertEqual(re.search('\\b(abc)\\b', 'abc').group(1), 'abc')
    ReTests.assertTrue(re.match('\\b', 'abc'))
    ReTests.assertTrue(re.search('\\B', 'abc'))
    ReTests.assertFalse(re.match('\\B', 'abc'))
    ReTests.assertIsNone(re.search('\\B', ''))
    ReTests.assertIsNone(re.search('\\b', ''))
    ReTests.assertEqual(len(re.findall('\\b', 'a')), 2)
    ReTests.assertEqual(len(re.findall('\\B', 'a')), 0)
    ReTests.assertEqual(len(re.findall('\\b', ' ')), 0)
    ReTests.assertEqual(len(re.findall('\\b', '   ')), 0)
    ReTests.assertEqual(len(re.findall('\\B', ' ')), 2)

ReTests = test_re.ReTests()
test_string_boundaries()
