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

def test_charmap():
    SurrogateEscapeTest.assertEqual(b'foo\xa5bar'.decode('iso-8859-3', 'surrogateescape'), 'foo\udca5bar')
    SurrogateEscapeTest.assertEqual('foo\udca5bar'.encode('iso-8859-3', 'surrogateescape'), b'foo\xa5bar')

SurrogateEscapeTest = test_codecs.SurrogateEscapeTest()
test_charmap()
