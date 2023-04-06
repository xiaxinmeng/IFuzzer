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

def test_re_groupref_exists():
    ReTests.assertEqual(re.match('^(\\()?([^()]+)(?(1)\\))$', '(a)').groups(), ('(', 'a'))
    ReTests.assertEqual(re.match('^(\\()?([^()]+)(?(1)\\))$', 'a').groups(), (None, 'a'))
    ReTests.assertIsNone(re.match('^(\\()?([^()]+)(?(1)\\))$', 'a)'))
    ReTests.assertIsNone(re.match('^(\\()?([^()]+)(?(1)\\))$', '(a'))
    ReTests.assertEqual(re.match('^(?:(a)|c)((?(1)b|d))$', 'ab').groups(), ('a', 'b'))
    ReTests.assertEqual(re.match('^(?:(a)|c)((?(1)b|d))$', 'cd').groups(), (None, 'd'))
    ReTests.assertEqual(re.match('^(?:(a)|c)((?(1)|d))$', 'cd').groups(), (None, 'd'))
    ReTests.assertEqual(re.match('^(?:(a)|c)((?(1)|d))$', 'a').groups(), ('a', ''))
    p = re.compile('(?P<g1>a)(?P<g2>b)?((?(g2)c|d))')
    ReTests.assertEqual(p.match('abc').groups(), ('a', 'b', 'c'))
    ReTests.assertEqual(p.match('ad').groups(), ('a', None, 'd'))
    ReTests.assertIsNone(p.match('abd'))
    ReTests.assertIsNone(p.match('ac'))
    pat = '|'.join(('x(?P<a%d>%x)y' % (i, i) for i in range(1, 200 + 1)))
    pat = '(?:%s)(?(200)z)' % pat
    ReTests.assertEqual(re.match(pat, 'xc8yz').span(), (0, 5))
    ReTests.checkPatternError('(?P<a>)(?(0))', 'bad group number', 10)
    ReTests.checkPatternError('()(?(1)a|b', 'missing ), unterminated subpattern', 2)
    ReTests.checkPatternError('()(?(1)a|b|c)', 'conditional backref with more than two branches', 10)

ReTests = test_re.ReTests()
test_re_groupref_exists()
