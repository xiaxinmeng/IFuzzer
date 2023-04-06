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

def test_qualified_re_split():
    ReTests.assertEqual(re.split(':', ':a:b::c', 2), ['', 'a', 'b::c'])
    ReTests.assertEqual(re.split(':', ':a:b::c', maxsplit=2), ['', 'a', 'b::c'])
    ReTests.assertEqual(re.split(':', 'a:b:c:d', maxsplit=2), ['a', 'b', 'c:d'])
    ReTests.assertEqual(re.split('(:)', ':a:b::c', maxsplit=2), ['', ':', 'a', ':', 'b::c'])
    ReTests.assertEqual(re.split('(:+)', ':a:b::c', maxsplit=2), ['', ':', 'a', ':', 'b::c'])
    ReTests.assertEqual(re.split('(:*)', ':a:b::c', maxsplit=2), ['', ':', '', '', 'a:b::c'])

ReTests = test_re.ReTests()
test_qualified_re_split()
