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

@unittest.skipUnless(sys.maxsize == 2 ** 31 - 1, 'requires 32-bit system')
@support.cpython_only
def test_case_operation_overflow():
    size = 2 ** 32 // 12 + 1
    try:
        s = 'ü' * size
    except MemoryError:
        UnicodeTest.skipTest('no enough memory (%.0f MiB required)' % (size / 2 ** 20))
    try:
        UnicodeTest.assertRaises(OverflowError, s.upper)
    finally:
        del s

UnicodeTest = test_unicode.UnicodeTest()
test_case_operation_overflow()
