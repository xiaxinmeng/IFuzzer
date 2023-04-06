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

def test_zerowidth():
    ReTests.assertEqual(re.split('\\b', 'a::bc'), ['', 'a', '::', 'bc', ''])
    ReTests.assertEqual(re.split('\\b|:+', 'a::bc'), ['', 'a', '', '', 'bc', ''])
    ReTests.assertEqual(re.split('(?<!\\w)(?=\\w)|:+', 'a::bc'), ['', 'a', '', 'bc'])
    ReTests.assertEqual(re.split('(?<=\\w)(?!\\w)|:+', 'a::bc'), ['a', '', 'bc', ''])
    ReTests.assertEqual(re.sub('\\b', '-', 'a::bc'), '-a-::-bc-')
    ReTests.assertEqual(re.sub('\\b|:+', '-', 'a::bc'), '-a---bc-')
    ReTests.assertEqual(re.sub('(\\b|:+)', '[\\1]', 'a::bc'), '[]a[][::][]bc[]')
    ReTests.assertEqual(re.findall('\\b|:+', 'a::bc'), ['', '', '::', '', ''])
    ReTests.assertEqual(re.findall('\\b|\\w+', 'a::bc'), ['', 'a', '', '', 'bc', ''])
    ReTests.assertEqual([m.span() for m in re.finditer('\\b|:+', 'a::bc')], [(0, 0), (1, 1), (1, 3), (3, 3), (5, 5)])
    ReTests.assertEqual([m.span() for m in re.finditer('\\b|\\w+', 'a::bc')], [(0, 0), (0, 1), (1, 1), (3, 3), (3, 5), (5, 5)])

ReTests = test_re.ReTests()
test_zerowidth()
