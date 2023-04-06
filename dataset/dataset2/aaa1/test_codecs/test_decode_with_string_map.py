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

def test_decode_with_string_map():
    CharmapTest.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'strict', 'abc'), ('abc', 3))
    CharmapTest.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'strict', '\U0010ffffbc'), ('\U0010ffffbc', 3))
    CharmapTest.assertRaises(UnicodeDecodeError, codecs.charmap_decode, b'\x00\x01\x02', 'strict', 'ab')
    CharmapTest.assertRaises(UnicodeDecodeError, codecs.charmap_decode, b'\x00\x01\x02', 'strict', 'ab\ufffe')
    CharmapTest.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'replace', 'ab'), ('ab�', 3))
    CharmapTest.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'replace', 'ab\ufffe'), ('ab�', 3))
    CharmapTest.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'backslashreplace', 'ab'), ('ab\\x02', 3))
    CharmapTest.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'backslashreplace', 'ab\ufffe'), ('ab\\x02', 3))
    CharmapTest.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'ignore', 'ab'), ('ab', 3))
    CharmapTest.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'ignore', 'ab\ufffe'), ('ab', 3))
    allbytes = bytes(range(256))
    CharmapTest.assertEqual(codecs.charmap_decode(allbytes, 'ignore', ''), ('', len(allbytes)))

CharmapTest = test_codecs.CharmapTest()
test_decode_with_string_map()
