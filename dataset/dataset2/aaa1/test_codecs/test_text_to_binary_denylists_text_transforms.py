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

def test_text_to_binary_denylists_text_transforms():
    msg = "^'rot_13' is not a text encoding; use codecs.encode\\(\\) to handle arbitrary codecs"
    with TransformCodecTest.assertRaisesRegex(LookupError, msg):
        'just an example message'.encode('rot_13')

TransformCodecTest = test_codecs.TransformCodecTest()
test_text_to_binary_denylists_text_transforms()
