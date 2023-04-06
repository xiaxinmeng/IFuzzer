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

def test_re_escape_non_ascii():
    s = 'xxx☠☠☠xxx'
    s_escaped = re.escape(s)
    ReTests.assertEqual(s_escaped, s)
    ReTests.assertMatch(s_escaped, s)
    ReTests.assertMatch('.%s+.' % re.escape('☠'), s, 'x☠☠☠x', (2, 7), re.search)

ReTests = test_re.ReTests()
test_re_escape_non_ascii()
