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

def test_find():
    string_tests.CommonTest.test_find()
    UnicodeTest.checkequal(100, 'a' * 100 + 'Ă', 'find', 'Ă')
    UnicodeTest.checkequal(-1, 'a' * 100 + 'Ă', 'find', 'ȁ')
    UnicodeTest.checkequal(-1, 'a' * 100 + 'Ă', 'find', 'Ġ')
    UnicodeTest.checkequal(-1, 'a' * 100 + 'Ă', 'find', 'Ƞ')
    UnicodeTest.checkequal(100, 'a' * 100 + '\U00100304', 'find', '\U00100304')
    UnicodeTest.checkequal(-1, 'a' * 100 + '\U00100304', 'find', '\U00100204')
    UnicodeTest.checkequal(-1, 'a' * 100 + '\U00100304', 'find', '\U00102004')
    UnicodeTest.checkequalnofix(0, 'abcdefghiabc', 'find', 'abc')
    UnicodeTest.checkequalnofix(9, 'abcdefghiabc', 'find', 'abc', 1)
    UnicodeTest.checkequalnofix(-1, 'abcdefghiabc', 'find', 'def', 4)
    UnicodeTest.assertRaises(TypeError, 'hello'.find)
    UnicodeTest.assertRaises(TypeError, 'hello'.find, 42)
    UnicodeTest.checkequal(100, 'Ă' * 100 + 'a', 'find', 'a')
    UnicodeTest.checkequal(100, '\U00100304' * 100 + 'a', 'find', 'a')
    UnicodeTest.checkequal(100, '\U00100304' * 100 + 'Ă', 'find', 'Ă')
    UnicodeTest.checkequal(-1, 'a' * 100, 'find', 'Ă')
    UnicodeTest.checkequal(-1, 'a' * 100, 'find', '\U00100304')
    UnicodeTest.checkequal(-1, 'Ă' * 100, 'find', '\U00100304')
    UnicodeTest.checkequal(100, 'Ă' * 100 + 'a_', 'find', 'a_')
    UnicodeTest.checkequal(100, '\U00100304' * 100 + 'a_', 'find', 'a_')
    UnicodeTest.checkequal(100, '\U00100304' * 100 + 'Ă_', 'find', 'Ă_')
    UnicodeTest.checkequal(-1, 'a' * 100, 'find', 'aĂ')
    UnicodeTest.checkequal(-1, 'a' * 100, 'find', 'a\U00100304')
    UnicodeTest.checkequal(-1, 'Ă' * 100, 'find', 'Ă\U00100304')

UnicodeTest = test_unicode.UnicodeTest()
test_find()
