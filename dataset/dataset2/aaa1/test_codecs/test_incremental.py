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

def test_incremental():
    decoded = codecs.code_page_decode(932, b'\x82', 'strict', False)
    CodePageTest.assertEqual(decoded, ('', 0))
    decoded = codecs.code_page_decode(932, b'\xe9\x80\xe9', 'strict', False)
    CodePageTest.assertEqual(decoded, ('騾', 2))
    decoded = codecs.code_page_decode(932, b'\xe9\x80\xe9\x80', 'strict', False)
    CodePageTest.assertEqual(decoded, ('騾騾', 4))
    decoded = codecs.code_page_decode(932, b'abc', 'strict', False)
    CodePageTest.assertEqual(decoded, ('abc', 3))

CodePageTest = test_codecs.CodePageTest()
test_incremental()
