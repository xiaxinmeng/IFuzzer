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

def test_codec_lookup_failure_not_wrapped():
    msg = '^unknown encoding: {}$'.format(ExceptionChainingTest.codec_name)
    with ExceptionChainingTest.assertRaisesRegex(LookupError, msg):
        'str input'.encode(ExceptionChainingTest.codec_name)
    with ExceptionChainingTest.assertRaisesRegex(LookupError, msg):
        codecs.encode('str input', ExceptionChainingTest.codec_name)
    with ExceptionChainingTest.assertRaisesRegex(LookupError, msg):
        b'bytes input'.decode(ExceptionChainingTest.codec_name)
    with ExceptionChainingTest.assertRaisesRegex(LookupError, msg):
        codecs.decode(b'bytes input', ExceptionChainingTest.codec_name)

ExceptionChainingTest = test_codecs.ExceptionChainingTest()
test_codec_lookup_failure_not_wrapped()
