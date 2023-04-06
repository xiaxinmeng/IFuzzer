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

def test_invalid_code_page():
    CodePageTest.assertRaises(ValueError, codecs.code_page_encode, -1, 'a')
    CodePageTest.assertRaises(ValueError, codecs.code_page_decode, -1, b'a')
    CodePageTest.assertRaises(OSError, codecs.code_page_encode, 123, 'a')
    CodePageTest.assertRaises(OSError, codecs.code_page_decode, 123, b'a')

CodePageTest = test_codecs.CodePageTest()
test_invalid_code_page()
