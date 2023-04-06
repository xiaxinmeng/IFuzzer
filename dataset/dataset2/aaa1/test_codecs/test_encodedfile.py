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

def test_encodedfile():
    f = io.BytesIO(b'\xc3\xbc')
    with codecs.EncodedFile(f, 'latin-1', 'utf-8') as ef:
        WithStmtTest.assertEqual(ef.read(), b'\xfc')
    WithStmtTest.assertTrue(f.closed)

WithStmtTest = test_codecs.WithStmtTest()
test_encodedfile()
