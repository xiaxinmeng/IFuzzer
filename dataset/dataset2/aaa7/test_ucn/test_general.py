import ast
import unittest
import unicodedata
from test import support
from http.client import HTTPException
from _testcapi import INT_MAX, PY_SSIZE_T_MAX, UINT_MAX
import test_ucn

def test_general():
    chars = ['LATIN CAPITAL LETTER T', 'LATIN SMALL LETTER H', 'LATIN SMALL LETTER E', 'SPACE', 'LATIN SMALL LETTER R', 'LATIN CAPITAL LETTER E', 'LATIN SMALL LETTER D', 'SPACE', 'LATIN SMALL LETTER f', 'LATIN CAPITAL LeTtEr o', 'LATIN SMaLl LETTER x', 'SPACE', 'LATIN SMALL LETTER A', 'LATIN SMALL LETTER T', 'LATIN SMALL LETTER E', 'SPACE', 'LATIN SMALL LETTER T', 'LATIN SMALL LETTER H', 'LATIN SMALL LETTER E', 'SpAcE', 'LATIN SMALL LETTER S', 'LATIN SMALL LETTER H', 'LATIN small LETTER e', 'LATIN small LETTER e', 'LATIN SMALL LETTER P', 'FULL STOP']
    string = 'The rEd fOx ate the sheep.'
    UnicodeNamesTest.assertEqual(''.join([UnicodeNamesTest.checkletter(*args) for args in zip(chars, string)]), string)

UnicodeNamesTest = test_ucn.UnicodeNamesTest()
test_general()
