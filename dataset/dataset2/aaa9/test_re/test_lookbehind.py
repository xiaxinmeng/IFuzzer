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

def test_lookbehind():
    ReTests.assertTrue(re.match('ab(?<=b)c', 'abc'))
    ReTests.assertIsNone(re.match('ab(?<=c)c', 'abc'))
    ReTests.assertIsNone(re.match('ab(?<!b)c', 'abc'))
    ReTests.assertTrue(re.match('ab(?<!c)c', 'abc'))
    ReTests.assertTrue(re.match('(a)a(?<=\\1)c', 'aac'))
    ReTests.assertIsNone(re.match('(a)b(?<=\\1)a', 'abaa'))
    ReTests.assertIsNone(re.match('(a)a(?<!\\1)c', 'aac'))
    ReTests.assertTrue(re.match('(a)b(?<!\\1)a', 'abaa'))
    ReTests.assertIsNone(re.match('(?:(a)|(x))b(?<=(?(2)x|c))c', 'abc'))
    ReTests.assertIsNone(re.match('(?:(a)|(x))b(?<=(?(2)b|x))c', 'abc'))
    ReTests.assertTrue(re.match('(?:(a)|(x))b(?<=(?(2)x|b))c', 'abc'))
    ReTests.assertIsNone(re.match('(?:(a)|(x))b(?<=(?(1)c|x))c', 'abc'))
    ReTests.assertTrue(re.match('(?:(a)|(x))b(?<=(?(1)b|x))c', 'abc'))
    ReTests.assertRaises(re.error, re.compile, '(a)b(?<=(?(2)b|x))(c)')
    ReTests.assertIsNone(re.match('(a)b(?<=(?(1)c|x))(c)', 'abc'))
    ReTests.assertTrue(re.match('(a)b(?<=(?(1)b|x))(c)', 'abc'))
    ReTests.assertRaises(re.error, re.compile, '(a)b(?<=(.)\\2)(c)')
    ReTests.assertRaises(re.error, re.compile, '(a)b(?<=(?P<a>.)(?P=a))(c)')
    ReTests.assertRaises(re.error, re.compile, '(a)b(?<=(a)(?(2)b|x))(c)')
    ReTests.assertRaises(re.error, re.compile, '(a)b(?<=(.)(?<=\\2))(c)')

ReTests = test_re.ReTests()
test_lookbehind()
