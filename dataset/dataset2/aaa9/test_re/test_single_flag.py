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

def test_single_flag():
    PatternReprTests.check_flags('random pattern', re.IGNORECASE, "re.compile('random pattern', re.IGNORECASE)")

PatternReprTests = test_re.PatternReprTests()
test_single_flag()
