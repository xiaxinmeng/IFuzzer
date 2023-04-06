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

def test_sub_template_numeric_escape():
    ReTests.assertEqual(re.sub('x', '\\0', 'x'), '\x00')
    ReTests.assertEqual(re.sub('x', '\\000', 'x'), '\x00')
    ReTests.assertEqual(re.sub('x', '\\001', 'x'), '\x01')
    ReTests.assertEqual(re.sub('x', '\\008', 'x'), '\x00' + '8')
    ReTests.assertEqual(re.sub('x', '\\009', 'x'), '\x00' + '9')
    ReTests.assertEqual(re.sub('x', '\\111', 'x'), 'I')
    ReTests.assertEqual(re.sub('x', '\\117', 'x'), 'O')
    ReTests.assertEqual(re.sub('x', '\\377', 'x'), 'ÿ')
    ReTests.assertEqual(re.sub('x', '\\1111', 'x'), 'I1')
    ReTests.assertEqual(re.sub('x', '\\1111', 'x'), 'I' + '1')
    ReTests.assertEqual(re.sub('x', '\\00', 'x'), '\x00')
    ReTests.assertEqual(re.sub('x', '\\07', 'x'), '\x07')
    ReTests.assertEqual(re.sub('x', '\\08', 'x'), '\x00' + '8')
    ReTests.assertEqual(re.sub('x', '\\09', 'x'), '\x00' + '9')
    ReTests.assertEqual(re.sub('x', '\\0a', 'x'), '\x00' + 'a')
    ReTests.checkTemplateError('x', '\\400', 'x', 'octal escape value \\400 outside of range 0-0o377', 0)
    ReTests.checkTemplateError('x', '\\777', 'x', 'octal escape value \\777 outside of range 0-0o377', 0)
    ReTests.checkTemplateError('x', '\\1', 'x', 'invalid group reference 1', 1)
    ReTests.checkTemplateError('x', '\\8', 'x', 'invalid group reference 8', 1)
    ReTests.checkTemplateError('x', '\\9', 'x', 'invalid group reference 9', 1)
    ReTests.checkTemplateError('x', '\\11', 'x', 'invalid group reference 11', 1)
    ReTests.checkTemplateError('x', '\\18', 'x', 'invalid group reference 18', 1)
    ReTests.checkTemplateError('x', '\\1a', 'x', 'invalid group reference 1', 1)
    ReTests.checkTemplateError('x', '\\90', 'x', 'invalid group reference 90', 1)
    ReTests.checkTemplateError('x', '\\99', 'x', 'invalid group reference 99', 1)
    ReTests.checkTemplateError('x', '\\118', 'x', 'invalid group reference 11', 1)
    ReTests.checkTemplateError('x', '\\11a', 'x', 'invalid group reference 11', 1)
    ReTests.checkTemplateError('x', '\\181', 'x', 'invalid group reference 18', 1)
    ReTests.checkTemplateError('x', '\\800', 'x', 'invalid group reference 80', 1)
    ReTests.checkTemplateError('x', '\\8', '', 'invalid group reference 8', 1)
    ReTests.assertEqual(re.sub('(((((((((((x)))))))))))', '\\11', 'x'), 'x')
    ReTests.assertEqual(re.sub('((((((((((y))))))))))(.)', '\\118', 'xyz'), 'xz8')
    ReTests.assertEqual(re.sub('((((((((((y))))))))))(.)', '\\11a', 'xyz'), 'xza')

ReTests = test_re.ReTests()
test_sub_template_numeric_escape()
