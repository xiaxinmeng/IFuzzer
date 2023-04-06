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

def test_long_pattern():
    pattern = 'Very %spattern' % ('long ' * 1000)
    r = repr(re.compile(pattern))
    PatternReprTests.assertLess(len(r), 300)
    PatternReprTests.assertEqual(r[:30], "re.compile('Very long long lon")
    r = repr(re.compile(pattern, re.I))
    PatternReprTests.assertLess(len(r), 300)
    PatternReprTests.assertEqual(r[:30], "re.compile('Very long long lon")
    PatternReprTests.assertEqual(r[-16:], ', re.IGNORECASE)')

PatternReprTests = test_re.PatternReprTests()
test_long_pattern()
