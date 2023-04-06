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

def test_re_groupref():
    ReTests.assertEqual(re.match('^(\\|)?([^()]+)\\1$', '|a|').groups(), ('|', 'a'))
    ReTests.assertEqual(re.match('^(\\|)?([^()]+)\\1?$', 'a').groups(), (None, 'a'))
    ReTests.assertIsNone(re.match('^(\\|)?([^()]+)\\1$', 'a|'))
    ReTests.assertIsNone(re.match('^(\\|)?([^()]+)\\1$', '|a'))
    ReTests.assertEqual(re.match('^(?:(a)|c)(\\1)$', 'aa').groups(), ('a', 'a'))
    ReTests.assertEqual(re.match('^(?:(a)|c)(\\1)?$', 'c').groups(), (None, None))
    ReTests.checkPatternError('(abc\\1)', 'cannot refer to an open group', 4)

ReTests = test_re.ReTests()
test_re_groupref()
