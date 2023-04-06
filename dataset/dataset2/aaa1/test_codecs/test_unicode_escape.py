import codecs
import contextlib
import io
import locale
import sys
import unittest
import encodings
from unittest import mock
from test import support
from test.support import os_helper
from test.support import warnings_helper
import _testcapi
import ctypes

from ctypes.wintypes import BOOL, UINT, BYTE, WCHAR, UINT, DWORD
import array
from encodings.idna import nameprep
from encodings import cp1140
import zlib

import test_codecs

def test_unicode_escape():
    TypesTest.assertEqual(codecs.unicode_escape_decode('\\u1234'), ('ሴ', 6))
    TypesTest.assertEqual(codecs.unicode_escape_decode(b'\\u1234'), ('ሴ', 6))
    TypesTest.assertEqual(codecs.raw_unicode_escape_decode('\\u1234'), ('ሴ', 6))
    TypesTest.assertEqual(codecs.raw_unicode_escape_decode(b'\\u1234'), ('ሴ', 6))
    TypesTest.assertRaises(UnicodeDecodeError, codecs.unicode_escape_decode, b'\\U00110000')
    TypesTest.assertEqual(codecs.unicode_escape_decode('\\U00110000', 'replace'), ('�', 10))
    TypesTest.assertEqual(codecs.unicode_escape_decode('\\U00110000', 'backslashreplace'), ('\\x5c\\x55\\x30\\x30\\x31\\x31\\x30\\x30\\x30\\x30', 10))
    TypesTest.assertRaises(UnicodeDecodeError, codecs.raw_unicode_escape_decode, b'\\U00110000')
    TypesTest.assertEqual(codecs.raw_unicode_escape_decode('\\U00110000', 'replace'), ('�', 10))
    TypesTest.assertEqual(codecs.raw_unicode_escape_decode('\\U00110000', 'backslashreplace'), ('\\x5c\\x55\\x30\\x30\\x31\\x31\\x30\\x30\\x30\\x30', 10))

TypesTest = test_codecs.TypesTest()
test_unicode_escape()
