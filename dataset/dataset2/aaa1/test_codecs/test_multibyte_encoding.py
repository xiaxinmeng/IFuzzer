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

def test_multibyte_encoding():
    CodePageTest.check_decode(932, ((b'\x84\xe9\x80', 'ignore', '騾'), (b'\x84\xe9\x80', 'replace', '�騾')))
    CodePageTest.check_decode(CodePageTest.CP_UTF8, ((b'\xff\xf4\x8f\xbf\xbf', 'ignore', '\U0010ffff'), (b'\xff\xf4\x8f\xbf\xbf', 'replace', '�\U0010ffff')))
    CodePageTest.check_encode(CodePageTest.CP_UTF8, (('[\U0010ffff\udc80]', 'ignore', b'[\xf4\x8f\xbf\xbf]'), ('[\U0010ffff\udc80]', 'replace', b'[\xf4\x8f\xbf\xbf?]')))

CodePageTest = test_codecs.CodePageTest()
test_multibyte_encoding()
