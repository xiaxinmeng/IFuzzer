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

def test_bad_decode_args():
    for encoding in test_codecs.all_unicode_encodings:
        decoder = codecs.getdecoder(encoding)
        BasicUnicodeTest.assertRaises(TypeError, decoder)
        if encoding not in ('idna', 'punycode'):
            BasicUnicodeTest.assertRaises(TypeError, decoder, 42)

BasicUnicodeTest = test_codecs.BasicUnicodeTest()
test_bad_decode_args()
