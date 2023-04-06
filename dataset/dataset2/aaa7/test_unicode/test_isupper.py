import _string
import codecs
import itertools
import operator
import struct
import sys
import textwrap
import unicodedata
import unittest
import warnings
from test.support import import_helper
from test.support import warnings_helper
from test import support, string_tests
from test.support.script_helper import assert_python_failure
import _testcapi
import datetime
import enum
from _testcapi import INT_MAX
from _testcapi import getargs_u
from ctypes import c_char_p, pythonapi, py_object, sizeof, c_int, c_long, c_longlong, c_ssize_t, c_uint, c_ulong, c_ulonglong, c_size_t, c_void_p
from _testcapi import unicode_aswidechar
from ctypes import c_wchar, sizeof
from _testcapi import unicode_aswidecharstring
from ctypes import c_wchar, sizeof
from _testcapi import unicode_asucs4
from _testcapi import unicode_asutf8
from _testcapi import unicode_asutf8andsize
from _testcapi import unicode_findchar
from _testcapi import unicode_copycharacters
from _testcapi import unicode_encodedecimal
from _testcapi import unicode_transformdecimaltoascii as transform_decimal
from _testcapi import getargs_s_hash
import test_unicode

def test_isupper():
    super().test_isupper()
    if not sys.platform.startswith('java'):
        UnicodeTest.checkequalnofix(False, 'ῼ', 'isupper')
    UnicodeTest.assertTrue('Ⅷ'.isupper())
    UnicodeTest.assertFalse('ⅷ'.isupper())
    UnicodeTest.assertTrue('𐐁'.isupper())
    UnicodeTest.assertTrue('𐐧'.isupper())
    UnicodeTest.assertFalse('𐐩'.isupper())
    UnicodeTest.assertFalse('𐑎'.isupper())
    UnicodeTest.assertFalse('🐍'.isupper())
    UnicodeTest.assertFalse('👯'.isupper())

UnicodeTest = test_unicode.UnicodeTest()
test_isupper()
