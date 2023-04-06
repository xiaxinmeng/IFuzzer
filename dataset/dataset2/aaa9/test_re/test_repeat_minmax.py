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

def test_repeat_minmax():
    ReTests.assertIsNone(re.match('^(\\w){1}$', 'abc'))
    ReTests.assertIsNone(re.match('^(\\w){1}?$', 'abc'))
    ReTests.assertIsNone(re.match('^(\\w){1,2}$', 'abc'))
    ReTests.assertIsNone(re.match('^(\\w){1,2}?$', 'abc'))
    ReTests.assertEqual(re.match('^(\\w){3}$', 'abc').group(1), 'c')
    ReTests.assertEqual(re.match('^(\\w){1,3}$', 'abc').group(1), 'c')
    ReTests.assertEqual(re.match('^(\\w){1,4}$', 'abc').group(1), 'c')
    ReTests.assertEqual(re.match('^(\\w){3,4}?$', 'abc').group(1), 'c')
    ReTests.assertEqual(re.match('^(\\w){3}?$', 'abc').group(1), 'c')
    ReTests.assertEqual(re.match('^(\\w){1,3}?$', 'abc').group(1), 'c')
    ReTests.assertEqual(re.match('^(\\w){1,4}?$', 'abc').group(1), 'c')
    ReTests.assertEqual(re.match('^(\\w){3,4}?$', 'abc').group(1), 'c')
    ReTests.assertIsNone(re.match('^x{1}$', 'xxx'))
    ReTests.assertIsNone(re.match('^x{1}?$', 'xxx'))
    ReTests.assertIsNone(re.match('^x{1,2}$', 'xxx'))
    ReTests.assertIsNone(re.match('^x{1,2}?$', 'xxx'))
    ReTests.assertTrue(re.match('^x{3}$', 'xxx'))
    ReTests.assertTrue(re.match('^x{1,3}$', 'xxx'))
    ReTests.assertTrue(re.match('^x{3,3}$', 'xxx'))
    ReTests.assertTrue(re.match('^x{1,4}$', 'xxx'))
    ReTests.assertTrue(re.match('^x{3,4}?$', 'xxx'))
    ReTests.assertTrue(re.match('^x{3}?$', 'xxx'))
    ReTests.assertTrue(re.match('^x{1,3}?$', 'xxx'))
    ReTests.assertTrue(re.match('^x{1,4}?$', 'xxx'))
    ReTests.assertTrue(re.match('^x{3,4}?$', 'xxx'))
    ReTests.assertIsNone(re.match('^x{}$', 'xxx'))
    ReTests.assertTrue(re.match('^x{}$', 'x{}'))
    ReTests.checkPatternError('x{2,1}', 'min repeat greater than max repeat', 2)

ReTests = test_re.ReTests()
test_repeat_minmax()
