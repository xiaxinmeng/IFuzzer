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

def test_encode_surrogateescape_error():
    with ASCIITest.assertRaises(UnicodeEncodeError):
        '\udc80€'.encode('latin1', 'surrogateescape')

ASCIITest = test_codecs.ASCIITest()
test_encode_surrogateescape_error()
