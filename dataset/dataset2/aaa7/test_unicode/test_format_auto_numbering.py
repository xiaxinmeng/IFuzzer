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

def test_format_auto_numbering():

    class C:

        def __init__(UnicodeTest, x=100):
            UnicodeTest._x = x

        def __format__(UnicodeTest, spec):
            return spec
    UnicodeTest.assertEqual('{}'.format(10), '10')
    UnicodeTest.assertEqual('{:5}'.format('s'), 's    ')
    UnicodeTest.assertEqual('{!r}'.format('s'), "'s'")
    UnicodeTest.assertEqual('{._x}'.format(C(10)), '10')
    UnicodeTest.assertEqual('{[1]}'.format([1, 2]), '2')
    UnicodeTest.assertEqual('{[a]}'.format({'a': 4, 'b': 2}), '4')
    UnicodeTest.assertEqual('a{}b{}c'.format(0, 1), 'a0b1c')
    UnicodeTest.assertEqual('a{:{}}b'.format('x', '^10'), 'a    x     b')
    UnicodeTest.assertEqual('a{:{}x}b'.format(20, '#'), 'a0x14b')
    UnicodeTest.assertRaises(ValueError, '{}{1}'.format, 1, 2)
    UnicodeTest.assertRaises(ValueError, '{1}{}'.format, 1, 2)
    UnicodeTest.assertRaises(ValueError, '{:{1}}'.format, 1, 2)
    UnicodeTest.assertRaises(ValueError, '{0:{}}'.format, 1, 2)
    UnicodeTest.assertEqual('{f}{}'.format(4, f='test'), 'test4')
    UnicodeTest.assertEqual('{}{f}'.format(4, f='test'), '4test')
    UnicodeTest.assertEqual('{:{f}}{g}{}'.format(1, 3, g='g', f=2), ' 1g3')
    UnicodeTest.assertEqual('{f:{}}{}{g}'.format(2, 4, f=1, g='g'), ' 14g')

UnicodeTest = test_unicode.UnicodeTest()
test_format_auto_numbering()
