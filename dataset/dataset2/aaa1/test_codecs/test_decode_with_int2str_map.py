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

def test_decode_with_int2str_map():
    CharmapTest.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'strict', {0: 'a', 1: 'b', 2: 'c'}), ('abc', 3))
    CharmapTest.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'strict', {0: 'Aa', 1: 'Bb', 2: 'Cc'}), ('AaBbCc', 3))
    CharmapTest.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'strict', {0: '\U0010ffff', 1: 'b', 2: 'c'}), ('\U0010ffffbc', 3))
    CharmapTest.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'strict', {0: 'a', 1: 'b', 2: ''}), ('ab', 3))
    CharmapTest.assertRaises(UnicodeDecodeError, codecs.charmap_decode, b'\x00\x01\x02', 'strict', {0: 'a', 1: 'b'})
    CharmapTest.assertRaises(UnicodeDecodeError, codecs.charmap_decode, b'\x00\x01\x02', 'strict', {0: 'a', 1: 'b', 2: None})
    CharmapTest.assertRaises(UnicodeDecodeError, codecs.charmap_decode, b'\x00\x01\x02', 'strict', {0: 'a', 1: 'b', 2: '\ufffe'})
    CharmapTest.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'replace', {0: 'a', 1: 'b'}), ('ab�', 3))
    CharmapTest.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'replace', {0: 'a', 1: 'b', 2: None}), ('ab�', 3))
    CharmapTest.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'replace', {0: 'a', 1: 'b', 2: '\ufffe'}), ('ab�', 3))
    CharmapTest.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'backslashreplace', {0: 'a', 1: 'b'}), ('ab\\x02', 3))
    CharmapTest.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'backslashreplace', {0: 'a', 1: 'b', 2: None}), ('ab\\x02', 3))
    CharmapTest.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'backslashreplace', {0: 'a', 1: 'b', 2: '\ufffe'}), ('ab\\x02', 3))
    CharmapTest.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'ignore', {0: 'a', 1: 'b'}), ('ab', 3))
    CharmapTest.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'ignore', {0: 'a', 1: 'b', 2: None}), ('ab', 3))
    CharmapTest.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'ignore', {0: 'a', 1: 'b', 2: '\ufffe'}), ('ab', 3))
    allbytes = bytes(range(256))
    CharmapTest.assertEqual(codecs.charmap_decode(allbytes, 'ignore', {}), ('', len(allbytes)))
    CharmapTest.assertRaisesRegex(TypeError, 'character mapping must be in range\\(0x110000\\)', codecs.charmap_decode, b'\x00\x01\x02', 'strict', {0: 'A', 1: 'Bb', 2: -2})
    CharmapTest.assertRaisesRegex(TypeError, 'character mapping must be in range\\(0x110000\\)', codecs.charmap_decode, b'\x00\x01\x02', 'strict', {0: 'A', 1: 'Bb', 2: 999999999})

CharmapTest = test_codecs.CharmapTest()
test_decode_with_int2str_map()
