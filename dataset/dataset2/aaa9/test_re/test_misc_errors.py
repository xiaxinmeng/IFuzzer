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

def test_misc_errors():
    ReTests.checkPatternError('(', 'missing ), unterminated subpattern', 0)
    ReTests.checkPatternError('((a|b)', 'missing ), unterminated subpattern', 0)
    ReTests.checkPatternError('(a|b))', 'unbalanced parenthesis', 5)
    ReTests.checkPatternError('(?P', 'unexpected end of pattern', 3)
    ReTests.checkPatternError('(?z)', 'unknown extension ?z', 1)
    ReTests.checkPatternError('(?iz)', 'unknown flag', 3)
    ReTests.checkPatternError('(?i', 'missing -, : or )', 3)
    ReTests.checkPatternError('(?#abc', 'missing ), unterminated comment', 0)
    ReTests.checkPatternError('(?<', 'unexpected end of pattern', 3)
    ReTests.checkPatternError('(?<>)', 'unknown extension ?<>', 1)
    ReTests.checkPatternError('(?', 'unexpected end of pattern', 2)

ReTests = test_re.ReTests()
test_misc_errors()
