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

def test_other_escapes():
    ReTests.checkPatternError('\\', 'bad escape (end of pattern)', 0)
    ReTests.assertEqual(re.match('\\(', '(').group(), '(')
    ReTests.assertIsNone(re.match('\\(', ')'))
    ReTests.assertEqual(re.match('\\\\', '\\').group(), '\\')
    ReTests.assertEqual(re.match('[\\]]', ']').group(), ']')
    ReTests.assertIsNone(re.match('[\\]]', '['))
    ReTests.assertEqual(re.match('[a\\-c]', '-').group(), '-')
    ReTests.assertIsNone(re.match('[a\\-c]', 'b'))
    ReTests.assertEqual(re.match('[\\^a]+', 'a^').group(), 'a^')
    ReTests.assertIsNone(re.match('[\\^a]+', 'b'))
    re.purge()
    for c in 'ceghijklmopqyzCEFGHIJKLMNOPQRTVXY':
        with ReTests.subTest(c):
            ReTests.assertRaises(re.error, re.compile, '\\%c' % c)
    for c in 'ceghijklmopqyzABCEFGHIJKLMNOPQRTVXYZ':
        with ReTests.subTest(c):
            ReTests.assertRaises(re.error, re.compile, '[\\%c]' % c)

ReTests = test_re.ReTests()
test_other_escapes()
