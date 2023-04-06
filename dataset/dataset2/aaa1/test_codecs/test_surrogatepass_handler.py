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

def test_surrogatepass_handler():
    UTF8Test.assertEqual('abc\ud800def'.encode(UTF8Test.encoding, 'surrogatepass'), UTF8Test.BOM + b'abc\xed\xa0\x80def')
    UTF8Test.assertEqual('\U00010fff\ud800'.encode(UTF8Test.encoding, 'surrogatepass'), UTF8Test.BOM + b'\xf0\x90\xbf\xbf\xed\xa0\x80')
    UTF8Test.assertEqual('[\ud800\udc80]'.encode(UTF8Test.encoding, 'surrogatepass'), UTF8Test.BOM + b'[\xed\xa0\x80\xed\xb2\x80]')
    UTF8Test.assertEqual(b'abc\xed\xa0\x80def'.decode(UTF8Test.encoding, 'surrogatepass'), 'abc\ud800def')
    UTF8Test.assertEqual(b'\xf0\x90\xbf\xbf\xed\xa0\x80'.decode(UTF8Test.encoding, 'surrogatepass'), '\U00010fff\ud800')
    UTF8Test.assertTrue(codecs.lookup_error('surrogatepass'))
    with UTF8Test.assertRaises(UnicodeDecodeError):
        b'abc\xed\xa0'.decode(UTF8Test.encoding, 'surrogatepass')
    with UTF8Test.assertRaises(UnicodeDecodeError):
        b'abc\xed\xa0z'.decode(UTF8Test.encoding, 'surrogatepass')

UTF8Test = test_codecs.UTF8Test()
test_surrogatepass_handler()
