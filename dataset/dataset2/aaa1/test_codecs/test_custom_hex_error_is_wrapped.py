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

def test_custom_hex_error_is_wrapped():
    msg = "^decoding with 'hex_codec' codec failed"
    with TransformCodecTest.assertRaisesRegex(Exception, msg) as failure:
        codecs.decode(b'hello', 'hex_codec')
    TransformCodecTest.assertIsInstance(failure.exception.__cause__, type(failure.exception))

TransformCodecTest = test_codecs.TransformCodecTest()
test_custom_hex_error_is_wrapped()
