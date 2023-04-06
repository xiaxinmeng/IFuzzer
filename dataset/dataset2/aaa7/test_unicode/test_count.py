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

def test_count():
    string_tests.CommonTest.test_count()
    UnicodeTest.checkequalnofix(3, 'aaa', 'count', 'a')
    UnicodeTest.checkequalnofix(0, 'aaa', 'count', 'b')
    UnicodeTest.checkequalnofix(3, 'aaa', 'count', 'a')
    UnicodeTest.checkequalnofix(0, 'aaa', 'count', 'b')
    UnicodeTest.checkequalnofix(0, 'aaa', 'count', 'b')
    UnicodeTest.checkequalnofix(1, 'aaa', 'count', 'a', -1)
    UnicodeTest.checkequalnofix(3, 'aaa', 'count', 'a', -10)
    UnicodeTest.checkequalnofix(2, 'aaa', 'count', 'a', 0, -1)
    UnicodeTest.checkequalnofix(0, 'aaa', 'count', 'a', 0, -10)
    UnicodeTest.checkequal(10, 'Ă' + 'a' * 10, 'count', 'a')
    UnicodeTest.checkequal(10, '\U00100304' + 'a' * 10, 'count', 'a')
    UnicodeTest.checkequal(10, '\U00100304' + 'Ă' * 10, 'count', 'Ă')
    UnicodeTest.checkequal(0, 'a' * 10, 'count', 'Ă')
    UnicodeTest.checkequal(0, 'a' * 10, 'count', '\U00100304')
    UnicodeTest.checkequal(0, 'Ă' * 10, 'count', '\U00100304')
    UnicodeTest.checkequal(10, 'Ă' + 'a_' * 10, 'count', 'a_')
    UnicodeTest.checkequal(10, '\U00100304' + 'a_' * 10, 'count', 'a_')
    UnicodeTest.checkequal(10, '\U00100304' + 'Ă_' * 10, 'count', 'Ă_')
    UnicodeTest.checkequal(0, 'a' * 10, 'count', 'aĂ')
    UnicodeTest.checkequal(0, 'a' * 10, 'count', 'a\U00100304')
    UnicodeTest.checkequal(0, 'Ă' * 10, 'count', 'Ă\U00100304')

UnicodeTest = test_unicode.UnicodeTest()
test_count()
