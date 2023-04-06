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

def test_repeat_minmax_overflow():
    string = 'x' * 100000
    ReTests.assertEqual(re.match('.{65535}', string).span(), (0, 65535))
    ReTests.assertEqual(re.match('.{,65535}', string).span(), (0, 65535))
    ReTests.assertEqual(re.match('.{65535,}?', string).span(), (0, 65535))
    ReTests.assertEqual(re.match('.{65536}', string).span(), (0, 65536))
    ReTests.assertEqual(re.match('.{,65536}', string).span(), (0, 65536))
    ReTests.assertEqual(re.match('.{65536,}?', string).span(), (0, 65536))
    ReTests.assertRaises(OverflowError, re.compile, '.{%d}' % 2 ** 128)
    ReTests.assertRaises(OverflowError, re.compile, '.{,%d}' % 2 ** 128)
    ReTests.assertRaises(OverflowError, re.compile, '.{%d,}?' % 2 ** 128)
    ReTests.assertRaises(OverflowError, re.compile, '.{%d,%d}' % (2 ** 129, 2 ** 128))

ReTests = test_re.ReTests()
test_repeat_minmax_overflow()
