import ast
import unittest
import unicodedata
from test import support
from http.client import HTTPException
from _testcapi import INT_MAX, PY_SSIZE_T_MAX, UINT_MAX
import test_ucn

def test_ascii_letters():
    for char in ''.join(map(chr, range(ord('a'), ord('z')))):
        name = 'LATIN SMALL LETTER %s' % char.upper()
        code = unicodedata.lookup(name)
        UnicodeNamesTest.assertEqual(unicodedata.name(code), name)

UnicodeNamesTest = test_ucn.UnicodeNamesTest()
test_ascii_letters()
