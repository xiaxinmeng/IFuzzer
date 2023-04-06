import ast
import unittest
import unicodedata
from test import support
from http.client import HTTPException
from _testcapi import INT_MAX, PY_SSIZE_T_MAX, UINT_MAX
import test_ucn

def test_named_sequences_names_in_pua_range():
    for cp in range(983296, 987135):
        with UnicodeNamesTest.assertRaises(ValueError) as cm:
            unicodedata.name(chr(cp))
        UnicodeNamesTest.assertEqual(str(cm.exception), 'no such name')

UnicodeNamesTest = test_ucn.UnicodeNamesTest()
test_named_sequences_names_in_pua_range()
