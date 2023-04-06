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

def test_utf8():
    SurrogateEscapeTest.assertEqual(b'foo\x80bar'.decode('utf-8', 'surrogateescape'), 'foo\udc80bar')
    SurrogateEscapeTest.assertEqual('foo\udc80bar'.encode('utf-8', 'surrogateescape'), b'foo\x80bar')
    SurrogateEscapeTest.assertEqual(b'\xed\xb0\x80'.decode('utf-8', 'surrogateescape'), '\udced\udcb0\udc80')
    SurrogateEscapeTest.assertEqual('\udced\udcb0\udc80'.encode('utf-8', 'surrogateescape'), b'\xed\xb0\x80')

SurrogateEscapeTest = test_codecs.SurrogateEscapeTest()
test_utf8()
