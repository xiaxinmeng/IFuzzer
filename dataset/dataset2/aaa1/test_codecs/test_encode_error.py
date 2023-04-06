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

def test_encode_error():
    for (data, error_handler, expected) in (('[\x80ÿ€]', 'ignore', b'[]'), ('[\x80ÿ€]', 'replace', b'[???]'), ('[\x80ÿ€]', 'xmlcharrefreplace', b'[&#128;&#255;&#8364;]'), ('[\x80ÿ€\U000abcde]', 'backslashreplace', b'[\\x80\\xff\\u20ac\\U000abcde]'), ('[\udc80\udcff]', 'surrogateescape', b'[\x80\xff]')):
        with ASCIITest.subTest(data=data, error_handler=error_handler, expected=expected):
            ASCIITest.assertEqual(data.encode('ascii', error_handler), expected)

ASCIITest = test_codecs.ASCIITest()
test_encode_error()
