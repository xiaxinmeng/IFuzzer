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

def test_cp1252():
    CodePageTest.check_encode(1252, (('abc', 'strict', b'abc'), ('é€', 'strict', b'\xe9\x80'), ('ÿ', 'strict', b'\xff'), ('Ł', 'strict', None), ('Ł', 'ignore', b''), ('Ł', 'replace', b'L'), ('\udc98', 'surrogateescape', b'\x98'), ('\udc98', 'surrogatepass', None)))
    CodePageTest.check_decode(1252, ((b'abc', 'strict', 'abc'), (b'\xe9\x80', 'strict', 'é€'), (b'\xff', 'strict', 'ÿ')))

CodePageTest = test_codecs.CodePageTest()
test_cp1252()
