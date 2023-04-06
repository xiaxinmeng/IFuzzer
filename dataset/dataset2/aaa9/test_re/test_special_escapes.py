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

def test_special_escapes():
    ReTests.assertEqual(re.search('\\b(b.)\\b', 'abcd abc bcd bx').group(1), 'bx')
    ReTests.assertEqual(re.search('\\B(b.)\\B', 'abc bcd bc abxd').group(1), 'bx')
    ReTests.assertEqual(re.search('\\b(b.)\\b', 'abcd abc bcd bx', re.ASCII).group(1), 'bx')
    ReTests.assertEqual(re.search('\\B(b.)\\B', 'abc bcd bc abxd', re.ASCII).group(1), 'bx')
    ReTests.assertEqual(re.search('^abc$', '\nabc\n', re.M).group(0), 'abc')
    ReTests.assertEqual(re.search('^\\Aabc\\Z$', 'abc', re.M).group(0), 'abc')
    ReTests.assertIsNone(re.search('^\\Aabc\\Z$', '\nabc\n', re.M))
    ReTests.assertEqual(re.search(b'\\b(b.)\\b', b'abcd abc bcd bx').group(1), b'bx')
    ReTests.assertEqual(re.search(b'\\B(b.)\\B', b'abc bcd bc abxd').group(1), b'bx')
    ReTests.assertEqual(re.search(b'\\b(b.)\\b', b'abcd abc bcd bx', re.LOCALE).group(1), b'bx')
    ReTests.assertEqual(re.search(b'\\B(b.)\\B', b'abc bcd bc abxd', re.LOCALE).group(1), b'bx')
    ReTests.assertEqual(re.search(b'^abc$', b'\nabc\n', re.M).group(0), b'abc')
    ReTests.assertEqual(re.search(b'^\\Aabc\\Z$', b'abc', re.M).group(0), b'abc')
    ReTests.assertIsNone(re.search(b'^\\Aabc\\Z$', b'\nabc\n', re.M))
    ReTests.assertEqual(re.search('\\d\\D\\w\\W\\s\\S', '1aa! a').group(0), '1aa! a')
    ReTests.assertEqual(re.search(b'\\d\\D\\w\\W\\s\\S', b'1aa! a').group(0), b'1aa! a')
    ReTests.assertEqual(re.search('\\d\\D\\w\\W\\s\\S', '1aa! a', re.ASCII).group(0), '1aa! a')
    ReTests.assertEqual(re.search(b'\\d\\D\\w\\W\\s\\S', b'1aa! a', re.LOCALE).group(0), b'1aa! a')

ReTests = test_re.ReTests()
test_special_escapes()
