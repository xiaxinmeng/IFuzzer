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

def test_cp932():
    CodePageTest.check_encode(932, (('abc', 'strict', b'abc'), ('ｄ騾', 'strict', b'\x82\x84\xe9\x80'), ('ÿ', 'strict', None), ('[ÿ]', 'ignore', b'[]'), ('[ÿ]', 'replace', b'[y]'), ('[€]', 'replace', b'[?]'), ('[ÿ]', 'backslashreplace', b'[\\xff]'), ('[ÿ]', 'namereplace', b'[\\N{LATIN SMALL LETTER Y WITH DIAERESIS}]'), ('[ÿ]', 'xmlcharrefreplace', b'[&#255;]'), ('\udcff', 'strict', None), ('[\udcff]', 'surrogateescape', b'[\xff]'), ('[\udcff]', 'surrogatepass', None)))
    CodePageTest.check_decode(932, ((b'abc', 'strict', 'abc'), (b'\x82\x84\xe9\x80', 'strict', 'ｄ騾'), (b'[\xff]', 'strict', None), (b'[\xff]', 'ignore', '[]'), (b'[\xff]', 'replace', '[�]'), (b'[\xff]', 'backslashreplace', '[\\xff]'), (b'[\xff]', 'surrogateescape', '[\udcff]'), (b'[\xff]', 'surrogatepass', None), (b'\x81\x00abc', 'strict', None), (b'\x81\x00abc', 'ignore', '\x00abc'), (b'\x81\x00abc', 'replace', '�\x00abc'), (b'\x81\x00abc', 'backslashreplace', '\\x81\x00abc')))

CodePageTest = test_codecs.CodePageTest()
test_cp932()
