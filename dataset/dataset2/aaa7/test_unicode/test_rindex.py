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

def test_rindex():
    string_tests.CommonTest.test_rindex()
    UnicodeTest.checkequalnofix(12, 'abcdefghiabc', 'rindex', '')
    UnicodeTest.checkequalnofix(3, 'abcdefghiabc', 'rindex', 'def')
    UnicodeTest.checkequalnofix(9, 'abcdefghiabc', 'rindex', 'abc')
    UnicodeTest.checkequalnofix(0, 'abcdefghiabc', 'rindex', 'abc', 0, -1)
    UnicodeTest.assertRaises(ValueError, 'abcdefghiabc'.rindex, 'hib')
    UnicodeTest.assertRaises(ValueError, 'defghiabc'.rindex, 'def', 1)
    UnicodeTest.assertRaises(ValueError, 'defghiabc'.rindex, 'abc', 0, -1)
    UnicodeTest.assertRaises(ValueError, 'abcdefghi'.rindex, 'ghi', 0, 8)
    UnicodeTest.assertRaises(ValueError, 'abcdefghi'.rindex, 'ghi', 0, -1)
    UnicodeTest.checkequal(0, 'a' + 'Ă' * 100, 'rindex', 'a')
    UnicodeTest.checkequal(0, 'a' + '\U00100304' * 100, 'rindex', 'a')
    UnicodeTest.checkequal(0, 'Ă' + '\U00100304' * 100, 'rindex', 'Ă')
    UnicodeTest.assertRaises(ValueError, ('a' * 100).rindex, 'Ă')
    UnicodeTest.assertRaises(ValueError, ('a' * 100).rindex, '\U00100304')
    UnicodeTest.assertRaises(ValueError, ('Ă' * 100).rindex, '\U00100304')
    UnicodeTest.checkequal(0, '_a' + 'Ă' * 100, 'rindex', '_a')
    UnicodeTest.checkequal(0, '_a' + '\U00100304' * 100, 'rindex', '_a')
    UnicodeTest.checkequal(0, '_Ă' + '\U00100304' * 100, 'rindex', '_Ă')
    UnicodeTest.assertRaises(ValueError, ('a' * 100).rindex, 'Ăa')
    UnicodeTest.assertRaises(ValueError, ('a' * 100).rindex, '\U00100304a')
    UnicodeTest.assertRaises(ValueError, ('Ă' * 100).rindex, '\U00100304Ă')

UnicodeTest = test_unicode.UnicodeTest()
test_rindex()
