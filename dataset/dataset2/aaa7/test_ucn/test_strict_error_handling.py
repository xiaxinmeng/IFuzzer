import ast
import unittest
import unicodedata
from test import support
from http.client import HTTPException
from _testcapi import INT_MAX, PY_SSIZE_T_MAX, UINT_MAX
import test_ucn

def test_strict_error_handling():
    UnicodeNamesTest.assertRaises(UnicodeError, str, b'\\N{blah}', 'unicode-escape', 'strict')
    UnicodeNamesTest.assertRaises(UnicodeError, str, bytes('\\N{%s}' % ('x' * 100000), 'ascii'), 'unicode-escape', 'strict')
    UnicodeNamesTest.assertRaises(UnicodeError, str, b'\\N{SPACE', 'unicode-escape', 'strict')
    UnicodeNamesTest.assertRaises(UnicodeError, str, b'\\NSPACE', 'unicode-escape', 'strict')

UnicodeNamesTest = test_ucn.UnicodeNamesTest()
test_strict_error_handling()
