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

def test_index():
    string_tests.CommonTest.test_index()
    UnicodeTest.checkequalnofix(0, 'abcdefghiabc', 'index', '')
    UnicodeTest.checkequalnofix(3, 'abcdefghiabc', 'index', 'def')
    UnicodeTest.checkequalnofix(0, 'abcdefghiabc', 'index', 'abc')
    UnicodeTest.checkequalnofix(9, 'abcdefghiabc', 'index', 'abc', 1)
    UnicodeTest.assertRaises(ValueError, 'abcdefghiabc'.index, 'hib')
    UnicodeTest.assertRaises(ValueError, 'abcdefghiab'.index, 'abc', 1)
    UnicodeTest.assertRaises(ValueError, 'abcdefghi'.index, 'ghi', 8)
    UnicodeTest.assertRaises(ValueError, 'abcdefghi'.index, 'ghi', -1)
    UnicodeTest.checkequal(100, 'Ă' * 100 + 'a', 'index', 'a')
    UnicodeTest.checkequal(100, '\U00100304' * 100 + 'a', 'index', 'a')
    UnicodeTest.checkequal(100, '\U00100304' * 100 + 'Ă', 'index', 'Ă')
    UnicodeTest.assertRaises(ValueError, ('a' * 100).index, 'Ă')
    UnicodeTest.assertRaises(ValueError, ('a' * 100).index, '\U00100304')
    UnicodeTest.assertRaises(ValueError, ('Ă' * 100).index, '\U00100304')
    UnicodeTest.checkequal(100, 'Ă' * 100 + 'a_', 'index', 'a_')
    UnicodeTest.checkequal(100, '\U00100304' * 100 + 'a_', 'index', 'a_')
    UnicodeTest.checkequal(100, '\U00100304' * 100 + 'Ă_', 'index', 'Ă_')
    UnicodeTest.assertRaises(ValueError, ('a' * 100).index, 'aĂ')
    UnicodeTest.assertRaises(ValueError, ('a' * 100).index, 'a\U00100304')
    UnicodeTest.assertRaises(ValueError, ('Ă' * 100).index, 'Ă\U00100304')

UnicodeTest = test_unicode.UnicodeTest()
test_index()
