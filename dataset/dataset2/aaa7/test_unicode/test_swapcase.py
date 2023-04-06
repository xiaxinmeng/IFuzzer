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

def test_swapcase():
    string_tests.CommonTest.test_swapcase()
    UnicodeTest.assertEqual('𐑏'.swapcase(), '𐐧')
    UnicodeTest.assertEqual('𐐧'.swapcase(), '𐑏')
    UnicodeTest.assertEqual('𐑏𐑏'.swapcase(), '𐐧𐐧')
    UnicodeTest.assertEqual('𐐧𐑏'.swapcase(), '𐑏𐐧')
    UnicodeTest.assertEqual('𐑏𐐧'.swapcase(), '𐐧𐑏')
    UnicodeTest.assertEqual('X𐐧x𐑏'.swapcase(), 'x𐑏X𐐧')
    UnicodeTest.assertEqual('ﬁ'.swapcase(), 'FI')
    UnicodeTest.assertEqual('İ'.swapcase(), 'i̇')
    UnicodeTest.assertEqual('Σ'.swapcase(), 'σ')
    UnicodeTest.assertEqual('ͅΣ'.swapcase(), 'Ισ')
    UnicodeTest.assertEqual('AͅΣ'.swapcase(), 'aΙς')
    UnicodeTest.assertEqual('AͅΣa'.swapcase(), 'aΙσA')
    UnicodeTest.assertEqual('AͅΣ'.swapcase(), 'aΙς')
    UnicodeTest.assertEqual('AΣͅ'.swapcase(), 'aςΙ')
    UnicodeTest.assertEqual('Σͅ '.swapcase(), 'σΙ ')
    UnicodeTest.assertEqual('Σ'.swapcase(), 'σ')
    UnicodeTest.assertEqual('ß'.swapcase(), 'SS')
    UnicodeTest.assertEqual('ῒ'.swapcase(), 'Ϊ̀')

UnicodeTest = test_unicode.UnicodeTest()
test_swapcase()
