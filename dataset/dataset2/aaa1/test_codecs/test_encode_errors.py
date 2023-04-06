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

def test_encode_errors():
    for (data, error_handler, expected) in (('[€\udc80]', 'ignore', b'[]'), ('[€\udc80]', 'replace', b'[??]'), ('[€\U000abcde]', 'backslashreplace', b'[\\u20ac\\U000abcde]'), ('[€\udc80]', 'xmlcharrefreplace', b'[&#8364;&#56448;]'), ('[\udc80\udcff]', 'surrogateescape', b'[\x80\xff]')):
        with Latin1Test.subTest(data=data, error_handler=error_handler, expected=expected):
            Latin1Test.assertEqual(data.encode('latin1', error_handler), expected)

Latin1Test = test_codecs.Latin1Test()
test_encode_errors()
