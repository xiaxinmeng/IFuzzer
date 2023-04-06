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

def test_code_page_name():
    CodePageTest.assertRaisesRegex(UnicodeEncodeError, 'cp932', codecs.code_page_encode, 932, 'ÿ')
    CodePageTest.assertRaisesRegex(UnicodeDecodeError, 'cp932', codecs.code_page_decode, 932, b'\x81\x00', 'strict', True)
    CodePageTest.assertRaisesRegex(UnicodeDecodeError, 'CP_UTF8', codecs.code_page_decode, CodePageTest.CP_UTF8, b'\xff', 'strict', True)

CodePageTest = test_codecs.CodePageTest()

test_code_page_name()
