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

def test_named_unicode_escapes():
    ReTests.assertTrue(re.match('\\N{LESS-THAN SIGN}', '<'))
    ReTests.assertTrue(re.match('\\N{less-than sign}', '<'))
    ReTests.assertIsNone(re.match('\\N{LESS-THAN SIGN}', '>'))
    ReTests.assertTrue(re.match('\\N{SNAKE}', '🐍'))
    ReTests.assertTrue(re.match('\\N{ARABIC LIGATURE UIGHUR KIRGHIZ YEH WITH HAMZA ABOVE WITH ALEF MAKSURA ISOLATED FORM}', 'ﯹ'))
    ReTests.assertTrue(re.match('[\\N{LESS-THAN SIGN}-\\N{GREATER-THAN SIGN}]', '='))
    ReTests.assertIsNone(re.match('[\\N{LESS-THAN SIGN}-\\N{GREATER-THAN SIGN}]', ';'))
    ReTests.checkPatternError('\\N', 'missing {', 2)
    ReTests.checkPatternError('[\\N]', 'missing {', 3)
    ReTests.checkPatternError('\\N{', 'missing character name', 3)
    ReTests.checkPatternError('[\\N{', 'missing character name', 4)
    ReTests.checkPatternError('\\N{}', 'missing character name', 3)
    ReTests.checkPatternError('[\\N{}]', 'missing character name', 4)
    ReTests.checkPatternError('\\NSNAKE}', 'missing {', 2)
    ReTests.checkPatternError('[\\NSNAKE}]', 'missing {', 3)
    ReTests.checkPatternError('\\N{SNAKE', 'missing }, unterminated name', 3)
    ReTests.checkPatternError('[\\N{SNAKE]', 'missing }, unterminated name', 4)
    ReTests.checkPatternError('[\\N{SNAKE]}', "undefined character name 'SNAKE]'", 1)
    ReTests.checkPatternError('\\N{SPAM}', "undefined character name 'SPAM'", 0)
    ReTests.checkPatternError('[\\N{SPAM}]', "undefined character name 'SPAM'", 1)
    ReTests.checkPatternError(b'\\N{LESS-THAN SIGN}', 'bad escape \\N', 0)
    ReTests.checkPatternError(b'[\\N{LESS-THAN SIGN}]', 'bad escape \\N', 1)

ReTests = test_re.ReTests()
test_named_unicode_escapes()
