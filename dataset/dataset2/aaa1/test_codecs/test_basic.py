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

def test_basic():
    f = io.BytesIO(b'\xed\x95\x9c\n\xea\xb8\x80')
    ef = codecs.EncodedFile(f, 'utf-16-le', 'utf-8')
    EncodedFileTest.assertEqual(ef.read(), b'\\\xd5\n\x00\x00\xae')
    f = io.BytesIO()
    ef = codecs.EncodedFile(f, 'utf-8', 'latin-1')
    ef.write(b'\xc3\xbc')
    EncodedFileTest.assertEqual(f.getvalue(), b'\xfc')

EncodedFileTest = test_codecs.EncodedFileTest()
test_basic()
