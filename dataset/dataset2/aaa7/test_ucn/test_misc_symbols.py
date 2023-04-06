import ast
import unittest
import unicodedata
from test import support
from http.client import HTTPException
from _testcapi import INT_MAX, PY_SSIZE_T_MAX, UINT_MAX
import test_ucn

def test_misc_symbols():
    UnicodeNamesTest.checkletter('PILCROW SIGN', '¶')
    UnicodeNamesTest.checkletter('REPLACEMENT CHARACTER', '�')
    UnicodeNamesTest.checkletter('HALFWIDTH KATAKANA SEMI-VOICED SOUND MARK', 'ﾟ')
    UnicodeNamesTest.checkletter('FULLWIDTH LATIN SMALL LETTER A', 'ａ')

UnicodeNamesTest = test_ucn.UnicodeNamesTest()
test_misc_symbols()
