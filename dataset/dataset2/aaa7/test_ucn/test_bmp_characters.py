import ast
import unittest
import unicodedata
from test import support
from http.client import HTTPException
from _testcapi import INT_MAX, PY_SSIZE_T_MAX, UINT_MAX
import test_ucn

def test_bmp_characters():
    for code in range(65536):
        char = chr(code)
        name = unicodedata.name(char, None)
        if name is not None:
            UnicodeNamesTest.assertEqual(unicodedata.lookup(name), char)

UnicodeNamesTest = test_ucn.UnicodeNamesTest()
test_bmp_characters()
