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

def test_lookahead():
    ReTests.assertEqual(re.match('(a(?=\\s[^a]))', 'a b').group(1), 'a')
    ReTests.assertEqual(re.match('(a(?=\\s[^a]*))', 'a b').group(1), 'a')
    ReTests.assertEqual(re.match('(a(?=\\s[abc]))', 'a b').group(1), 'a')
    ReTests.assertEqual(re.match('(a(?=\\s[abc]*))', 'a bc').group(1), 'a')
    ReTests.assertEqual(re.match('(a)(?=\\s\\1)', 'a a').group(1), 'a')
    ReTests.assertEqual(re.match('(a)(?=\\s\\1*)', 'a aa').group(1), 'a')
    ReTests.assertEqual(re.match('(a)(?=\\s(abc|a))', 'a a').group(1), 'a')
    ReTests.assertEqual(re.match('(a(?!\\s[^a]))', 'a a').group(1), 'a')
    ReTests.assertEqual(re.match('(a(?!\\s[abc]))', 'a d').group(1), 'a')
    ReTests.assertEqual(re.match('(a)(?!\\s\\1)', 'a b').group(1), 'a')
    ReTests.assertEqual(re.match('(a)(?!\\s(abc|a))', 'a b').group(1), 'a')
    ReTests.assertTrue(re.match('(a)b(?=\\1)a', 'aba'))
    ReTests.assertIsNone(re.match('(a)b(?=\\1)c', 'abac'))
    ReTests.assertTrue(re.match('(?:(a)|(x))b(?=(?(2)x|c))c', 'abc'))
    ReTests.assertIsNone(re.match('(?:(a)|(x))b(?=(?(2)c|x))c', 'abc'))
    ReTests.assertTrue(re.match('(?:(a)|(x))b(?=(?(2)x|c))c', 'abc'))
    ReTests.assertIsNone(re.match('(?:(a)|(x))b(?=(?(1)b|x))c', 'abc'))
    ReTests.assertTrue(re.match('(?:(a)|(x))b(?=(?(1)c|x))c', 'abc'))
    ReTests.assertTrue(re.match('(a)b(?=(?(2)x|c))(c)', 'abc'))
    ReTests.assertIsNone(re.match('(a)b(?=(?(2)b|x))(c)', 'abc'))
    ReTests.assertTrue(re.match('(a)b(?=(?(1)c|x))(c)', 'abc'))

ReTests = test_re.ReTests()
test_lookahead()
