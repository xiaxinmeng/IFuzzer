import ast
import unittest
import unicodedata
from test import support
from http.client import HTTPException
from _testcapi import INT_MAX, PY_SSIZE_T_MAX, UINT_MAX
import test_ucn

def test_cjk_unified_ideographs():
    UnicodeNamesTest.checkletter('CJK UNIFIED IDEOGRAPH-3400', '㐀')
    UnicodeNamesTest.checkletter('CJK UNIFIED IDEOGRAPH-4DB5', '䶵')
    UnicodeNamesTest.checkletter('CJK UNIFIED IDEOGRAPH-4E00', '一')
    UnicodeNamesTest.checkletter('CJK UNIFIED IDEOGRAPH-9FCB', '鿋')
    UnicodeNamesTest.checkletter('CJK UNIFIED IDEOGRAPH-20000', '𠀀')
    UnicodeNamesTest.checkletter('CJK UNIFIED IDEOGRAPH-2A6D6', '𪛖')
    UnicodeNamesTest.checkletter('CJK UNIFIED IDEOGRAPH-2A700', '𪜀')
    UnicodeNamesTest.checkletter('CJK UNIFIED IDEOGRAPH-2B734', '𫜴')
    UnicodeNamesTest.checkletter('CJK UNIFIED IDEOGRAPH-2B740', '𫝀')
    UnicodeNamesTest.checkletter('CJK UNIFIED IDEOGRAPH-2B81D', '𫠝')
    UnicodeNamesTest.checkletter('CJK UNIFIED IDEOGRAPH-3134A', '𱍊')

UnicodeNamesTest = test_ucn.UnicodeNamesTest()
test_cjk_unified_ideographs()
