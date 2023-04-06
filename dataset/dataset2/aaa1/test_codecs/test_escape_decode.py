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

def test_escape_decode():
    decode = codecs.raw_unicode_escape_decode
    check = test_codecs.coding_checker(UnicodeEscapeTest, decode)
    for b in range(256):
        if b not in b'uU':
            check(b'\\' + bytes([b]), '\\' + chr(b))
    check(b'\\u20ac', '€')
    check(b'\\U0001d120', '𝄠')

UnicodeEscapeTest = test_codecs.UnicodeEscapeTest()
test_escape_decode()
