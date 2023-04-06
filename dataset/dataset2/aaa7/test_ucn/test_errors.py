import ast
import unittest
import unicodedata
from test import support
from http.client import HTTPException
from _testcapi import INT_MAX, PY_SSIZE_T_MAX, UINT_MAX
import test_ucn

def test_errors():
    UnicodeNamesTest.assertRaises(TypeError, unicodedata.name)
    UnicodeNamesTest.assertRaises(TypeError, unicodedata.name, 'xx')
    UnicodeNamesTest.assertRaises(TypeError, unicodedata.lookup)
    UnicodeNamesTest.assertRaises(KeyError, unicodedata.lookup, 'unknown')

UnicodeNamesTest = test_ucn.UnicodeNamesTest()
test_errors()
