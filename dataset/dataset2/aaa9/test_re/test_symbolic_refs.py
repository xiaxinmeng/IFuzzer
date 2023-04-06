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

def test_symbolic_refs():
    ReTests.checkTemplateError('(?P<a>x)', '\\g<a', 'xx', 'missing >, unterminated name', 3)
    ReTests.checkTemplateError('(?P<a>x)', '\\g<', 'xx', 'missing group name', 3)
    ReTests.checkTemplateError('(?P<a>x)', '\\g', 'xx', 'missing <', 2)
    ReTests.checkTemplateError('(?P<a>x)', '\\g<a a>', 'xx', "bad character in group name 'a a'", 3)
    ReTests.checkTemplateError('(?P<a>x)', '\\g<>', 'xx', 'missing group name', 3)
    ReTests.checkTemplateError('(?P<a>x)', '\\g<1a1>', 'xx', "bad character in group name '1a1'", 3)
    ReTests.checkTemplateError('(?P<a>x)', '\\g<2>', 'xx', 'invalid group reference 2', 3)
    ReTests.checkTemplateError('(?P<a>x)', '\\2', 'xx', 'invalid group reference 2', 1)
    with ReTests.assertRaisesRegex(IndexError, "unknown group name 'ab'"):
        re.sub('(?P<a>x)', '\\g<ab>', 'xx')
    ReTests.assertEqual(re.sub('(?P<a>x)|(?P<b>y)', '\\g<b>', 'xx'), '')
    ReTests.assertEqual(re.sub('(?P<a>x)|(?P<b>y)', '\\2', 'xx'), '')
    ReTests.checkTemplateError('(?P<a>x)', '\\g<-1>', 'xx', "bad character in group name '-1'", 3)
    ReTests.assertEqual(re.sub('(?P<µ>x)', '\\g<µ>', 'xx'), 'xx')
    ReTests.assertEqual(re.sub('(?P<𝔘𝔫𝔦𝔠𝔬𝔡𝔢>x)', '\\g<𝔘𝔫𝔦𝔠𝔬𝔡𝔢>', 'xx'), 'xx')
    ReTests.checkTemplateError('(?P<a>x)', '\\g<©>', 'xx', "bad character in group name '©'", 3)
    pat = '|'.join(('x(?P<a%d>%x)y' % (i, i) for i in range(1, 200 + 1)))
    ReTests.assertEqual(re.sub(pat, '\\g<200>', 'xc8yzxc8y'), 'c8zc8')

ReTests = test_re.ReTests()
test_symbolic_refs()
