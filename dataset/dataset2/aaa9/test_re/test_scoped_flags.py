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

def test_scoped_flags():
    ReTests.assertTrue(re.match('(?i:a)b', 'Ab'))
    ReTests.assertIsNone(re.match('(?i:a)b', 'aB'))
    ReTests.assertIsNone(re.match('(?-i:a)b', 'Ab', re.IGNORECASE))
    ReTests.assertTrue(re.match('(?-i:a)b', 'aB', re.IGNORECASE))
    ReTests.assertIsNone(re.match('(?i:(?-i:a)b)', 'Ab'))
    ReTests.assertTrue(re.match('(?i:(?-i:a)b)', 'aB'))
    ReTests.assertTrue(re.match('(?x: a) b', 'a b'))
    ReTests.assertIsNone(re.match('(?x: a) b', ' a b'))
    ReTests.assertTrue(re.match('(?-x: a) b', ' ab', re.VERBOSE))
    ReTests.assertIsNone(re.match('(?-x: a) b', 'ab', re.VERBOSE))
    ReTests.assertTrue(re.match('\\w(?a:\\W)\\w', 'ààà'))
    ReTests.assertTrue(re.match('(?a:\\W(?u:\\w)\\W)', 'ààà'))
    ReTests.assertTrue(re.match('\\W(?u:\\w)\\W', 'ààà', re.ASCII))
    ReTests.checkPatternError('(?a)(?-a:\\w)', "bad inline flags: cannot turn off flags 'a', 'u' and 'L'", 8)
    ReTests.checkPatternError('(?i-i:a)', 'bad inline flags: flag turned on and off', 5)
    ReTests.checkPatternError('(?au:a)', "bad inline flags: flags 'a', 'u' and 'L' are incompatible", 4)
    ReTests.checkPatternError(b'(?aL:a)', "bad inline flags: flags 'a', 'u' and 'L' are incompatible", 4)
    ReTests.checkPatternError('(?-', 'missing flag', 3)
    ReTests.checkPatternError('(?-+', 'missing flag', 3)
    ReTests.checkPatternError('(?-z', 'unknown flag', 3)
    ReTests.checkPatternError('(?-i', 'missing :', 4)
    ReTests.checkPatternError('(?-i)', 'missing :', 4)
    ReTests.checkPatternError('(?-i+', 'missing :', 4)
    ReTests.checkPatternError('(?-iz', 'unknown flag', 4)
    ReTests.checkPatternError('(?i:', 'missing ), unterminated subpattern', 0)
    ReTests.checkPatternError('(?i', 'missing -, : or )', 3)
    ReTests.checkPatternError('(?i+', 'missing -, : or )', 3)
    ReTests.checkPatternError('(?iz', 'unknown flag', 3)

ReTests = test_re.ReTests()
test_scoped_flags()
