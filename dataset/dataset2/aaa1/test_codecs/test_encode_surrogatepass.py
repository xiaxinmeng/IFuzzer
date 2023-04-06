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

def test_encode_surrogatepass():
    try:
        LocaleCodecTest.encode('', 'surrogatepass')
    except ValueError as exc:
        if str(exc) == 'unsupported error handler':
            LocaleCodecTest.skipTest(f"{LocaleCodecTest.ENCODING!r} encoder doesn't support surrogatepass error handler")
        else:
            raise
    LocaleCodecTest.check_encode_strings('surrogatepass')

LocaleCodecTest = test_codecs.LocaleCodecTest()
test_encode_surrogatepass()
