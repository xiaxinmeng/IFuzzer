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

def test_codecs_utf8():
    UnicodeTest.assertEqual(''.encode('utf-8'), b'')
    UnicodeTest.assertEqual('€'.encode('utf-8'), b'\xe2\x82\xac')
    UnicodeTest.assertEqual('𐀂'.encode('utf-8'), b'\xf0\x90\x80\x82')
    UnicodeTest.assertEqual('𣑖'.encode('utf-8'), b'\xf0\xa3\x91\x96')
    UnicodeTest.assertEqual('\ud800'.encode('utf-8', 'surrogatepass'), b'\xed\xa0\x80')
    UnicodeTest.assertEqual('\udc00'.encode('utf-8', 'surrogatepass'), b'\xed\xb0\x80')
    UnicodeTest.assertEqual(('𐀂' * 10).encode('utf-8'), b'\xf0\x90\x80\x82' * 10)
    UnicodeTest.assertEqual('正確に言うと翻訳はされていません。一部はドイツ語ですが、あとはでたらめです。実際には「Wenn ist das Nunstuck git und'.encode('utf-8'), b'\xe6\xad\xa3\xe7\xa2\xba\xe3\x81\xab\xe8\xa8\x80\xe3\x81\x86\xe3\x81\xa8\xe7\xbf\xbb\xe8\xa8\xb3\xe3\x81\xaf\xe3\x81\x95\xe3\x82\x8c\xe3\x81\xa6\xe3\x81\x84\xe3\x81\xbe\xe3\x81\x9b\xe3\x82\x93\xe3\x80\x82\xe4\xb8\x80\xe9\x83\xa8\xe3\x81\xaf\xe3\x83\x89\xe3\x82\xa4\xe3\x83\x84\xe8\xaa\x9e\xe3\x81\xa7\xe3\x81\x99\xe3\x81\x8c\xe3\x80\x81\xe3\x81\x82\xe3\x81\xa8\xe3\x81\xaf\xe3\x81\xa7\xe3\x81\x9f\xe3\x82\x89\xe3\x82\x81\xe3\x81\xa7\xe3\x81\x99\xe3\x80\x82\xe5\xae\x9f\xe9\x9a\x9b\xe3\x81\xab\xe3\x81\xaf\xe3\x80\x8cWenn ist das Nunstuck git und')
    UnicodeTest.assertEqual(str(b'\xf0\xa3\x91\x96', 'utf-8'), '𣑖')
    UnicodeTest.assertEqual(str(b'\xf0\x90\x80\x82', 'utf-8'), '𐀂')
    UnicodeTest.assertEqual(str(b'\xe2\x82\xac', 'utf-8'), '€')

UnicodeTest = test_unicode.UnicodeTest()
test_codecs_utf8()
