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

def test_formatting_with_enum():
    import enum

    class Float(float, enum.Enum):
        PI = 3.1415926

    class Int(enum.IntEnum):
        IDES = 15

    class Str(str, enum.Enum):
        ABC = 'abc'
    UnicodeTest.assertEqual('%s, %s' % (Str.ABC, Str.ABC), 'Str.ABC, Str.ABC')
    UnicodeTest.assertEqual('%s, %s, %d, %i, %u, %f, %5.2f' % (Str.ABC, Str.ABC, Int.IDES, Int.IDES, Int.IDES, Float.PI, Float.PI), 'Str.ABC, Str.ABC, 15, 15, 15, 3.141593,  3.14')
    UnicodeTest.assertEqual('...%(foo)s...' % {'foo': Str.ABC}, '...Str.ABC...')
    UnicodeTest.assertEqual('...%(foo)s...' % {'foo': Int.IDES}, '...Int.IDES...')
    UnicodeTest.assertEqual('...%(foo)i...' % {'foo': Int.IDES}, '...15...')
    UnicodeTest.assertEqual('...%(foo)d...' % {'foo': Int.IDES}, '...15...')
    UnicodeTest.assertEqual('...%(foo)u...' % {'foo': Int.IDES, 'def': Float.PI}, '...15...')
    UnicodeTest.assertEqual('...%(foo)f...' % {'foo': Float.PI, 'def': 123}, '...3.141593...')

UnicodeTest = test_unicode.UnicodeTest()
test_formatting_with_enum()
