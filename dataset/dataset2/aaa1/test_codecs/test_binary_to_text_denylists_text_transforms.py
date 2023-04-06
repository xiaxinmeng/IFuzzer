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

def test_binary_to_text_denylists_text_transforms():
    for bad_input in (b'immutable', bytearray(b'mutable')):
        with TransformCodecTest.subTest(bad_input=bad_input):
            msg = "^'rot_13' is not a text encoding; use codecs.decode\\(\\) to handle arbitrary codecs"
            with TransformCodecTest.assertRaisesRegex(LookupError, msg) as failure:
                bad_input.decode('rot_13')
            TransformCodecTest.assertIsNone(failure.exception.__cause__)

TransformCodecTest = test_codecs.TransformCodecTest()
test_binary_to_text_denylists_text_transforms()
