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

def test_join():
    string_tests.MixinStrUnicodeUserStringTest.test_join()

    class MyWrapper:

        def __init__(UnicodeTest, sval):
            UnicodeTest.sval = sval

        def __str__(UnicodeTest):
            return UnicodeTest.sval
    UnicodeTest.checkequalnofix('a b c d', ' ', 'join', ['a', 'b', 'c', 'd'])
    UnicodeTest.checkequalnofix('abcd', '', 'join', ('a', 'b', 'c', 'd'))
    UnicodeTest.checkequalnofix('w x y z', ' ', 'join', string_tests.Sequence('wxyz'))
    UnicodeTest.checkequalnofix('a b c d', ' ', 'join', ['a', 'b', 'c', 'd'])
    UnicodeTest.checkequalnofix('a b c d', ' ', 'join', ['a', 'b', 'c', 'd'])
    UnicodeTest.checkequalnofix('abcd', '', 'join', ('a', 'b', 'c', 'd'))
    UnicodeTest.checkequalnofix('w x y z', ' ', 'join', string_tests.Sequence('wxyz'))
    UnicodeTest.checkraises(TypeError, ' ', 'join', ['1', '2', MyWrapper('foo')])
    UnicodeTest.checkraises(TypeError, ' ', 'join', ['1', '2', '3', bytes()])
    UnicodeTest.checkraises(TypeError, ' ', 'join', [1, 2, 3])
    UnicodeTest.checkraises(TypeError, ' ', 'join', ['1', '2', 3])

UnicodeTest = test_unicode.UnicodeTest()
test_join()
