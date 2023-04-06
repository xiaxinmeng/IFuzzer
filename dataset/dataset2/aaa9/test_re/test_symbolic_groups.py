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

def test_symbolic_groups():
    re.compile('(?P<a>x)(?P=a)(?(a)y)')
    re.compile('(?P<a1>x)(?P=a1)(?(a1)y)')
    re.compile('(?P<a1>x)\\1(?(1)y)')
    ReTests.checkPatternError('(?P<a>)(?P<a>)', "redefinition of group name 'a' as group 2; was group 1")
    ReTests.checkPatternError('(?P<a>(?P=a))', 'cannot refer to an open group', 10)
    ReTests.checkPatternError('(?Pxy)', 'unknown extension ?Px')
    ReTests.checkPatternError('(?P<a>)(?P=a', 'missing ), unterminated name', 11)
    ReTests.checkPatternError('(?P=', 'missing group name', 4)
    ReTests.checkPatternError('(?P=)', 'missing group name', 4)
    ReTests.checkPatternError('(?P=1)', "bad character in group name '1'", 4)
    ReTests.checkPatternError('(?P=a)', "unknown group name 'a'")
    ReTests.checkPatternError('(?P=a1)', "unknown group name 'a1'")
    ReTests.checkPatternError('(?P=a.)', "bad character in group name 'a.'", 4)
    ReTests.checkPatternError('(?P<)', 'missing >, unterminated name', 4)
    ReTests.checkPatternError('(?P<a', 'missing >, unterminated name', 4)
    ReTests.checkPatternError('(?P<', 'missing group name', 4)
    ReTests.checkPatternError('(?P<>)', 'missing group name', 4)
    ReTests.checkPatternError('(?P<1>)', "bad character in group name '1'", 4)
    ReTests.checkPatternError('(?P<a.>)', "bad character in group name 'a.'", 4)
    ReTests.checkPatternError('(?(', 'missing group name', 3)
    ReTests.checkPatternError('(?())', 'missing group name', 3)
    ReTests.checkPatternError('(?(a))', "unknown group name 'a'", 3)
    ReTests.checkPatternError('(?(-1))', "bad character in group name '-1'", 3)
    ReTests.checkPatternError('(?(1a))', "bad character in group name '1a'", 3)
    ReTests.checkPatternError('(?(a.))', "bad character in group name 'a.'", 3)
    re.compile('(?P<µ>x)(?P=µ)(?(µ)y)')
    re.compile('(?P<𝔘𝔫𝔦𝔠𝔬𝔡𝔢>x)(?P=𝔘𝔫𝔦𝔠𝔬𝔡𝔢)(?(𝔘𝔫𝔦𝔠𝔬𝔡𝔢)y)')
    ReTests.checkPatternError('(?P<©>x)', "bad character in group name '©'", 4)
    pat = '|'.join(('x(?P<a%d>%x)y' % (i, i) for i in range(1, 200 + 1)))
    pat = '(?:%s)(?(200)z|t)' % pat
    ReTests.assertEqual(re.match(pat, 'xc8yz').span(), (0, 5))

ReTests = test_re.ReTests()
test_symbolic_groups()
