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

def test_unexpected_end_of_data():
    """
        Test that an 'unexpected end of data' error is raised when the string
        ends after a start byte of a 2-, 3-, or 4-bytes sequence without having
        enough continuation bytes.  The incomplete sequence is replaced with a
        single U+FFFD when errors='replace'.
        E.g. in the sequence <F3 80 80>, F3 is the start byte of a 4-bytes
        sequence, but it's followed by only 2 valid continuation bytes and the
        last continuation bytes is missing.
        Note: the continuation bytes must be all valid, if one of them is
        invalid another error will be raised.
        """
    sequences = ['C2', 'DF', 'E0 A0', 'E0 BF', 'E1 80', 'E1 BF', 'EC 80', 'EC BF', 'ED 80', 'ED 9F', 'EE 80', 'EE BF', 'EF 80', 'EF BF', 'F0 90', 'F0 BF', 'F0 90 80', 'F0 90 BF', 'F0 BF 80', 'F0 BF BF', 'F1 80', 'F1 BF', 'F1 80 80', 'F1 80 BF', 'F1 BF 80', 'F1 BF BF', 'F3 80', 'F3 BF', 'F3 80 80', 'F3 80 BF', 'F3 BF 80', 'F3 BF BF', 'F4 80', 'F4 8F', 'F4 80 80', 'F4 80 BF', 'F4 8F 80', 'F4 8F BF']
    FFFD = '�'
    for seq in sequences:
        UnicodeTest.assertCorrectUTF8Decoding(bytes.fromhex(seq), '�', 'unexpected end of data')

UnicodeTest = test_unicode.UnicodeTest()
test_unexpected_end_of_data()
