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

def test_lower():
    string_tests.CommonTest.test_lower()
    UnicodeTest.assertEqual('𐐧'.lower(), '𐑏')
    UnicodeTest.assertEqual('𐐧𐐧'.lower(), '𐑏𐑏')
    UnicodeTest.assertEqual('𐐧𐑏'.lower(), '𐑏𐑏')
    UnicodeTest.assertEqual('X𐐧x𐑏'.lower(), 'x𐑏x𐑏')
    UnicodeTest.assertEqual('ﬁ'.lower(), 'ﬁ')
    UnicodeTest.assertEqual('İ'.lower(), 'i̇')
    UnicodeTest.assertEqual('Σ'.lower(), 'σ')
    UnicodeTest.assertEqual('ͅΣ'.lower(), 'ͅσ')
    UnicodeTest.assertEqual('AͅΣ'.lower(), 'aͅς')
    UnicodeTest.assertEqual('AͅΣa'.lower(), 'aͅσa')
    UnicodeTest.assertEqual('AͅΣ'.lower(), 'aͅς')
    UnicodeTest.assertEqual('AΣͅ'.lower(), 'aςͅ')
    UnicodeTest.assertEqual('Σͅ '.lower(), 'σͅ ')
    UnicodeTest.assertEqual('\U0008fffe'.lower(), '\U0008fffe')
    UnicodeTest.assertEqual('ⅷ'.lower(), 'ⅷ')

UnicodeTest = test_unicode.UnicodeTest()
test_lower()
