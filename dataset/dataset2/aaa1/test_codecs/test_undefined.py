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

def test_undefined():
    CodecsModuleTest.assertRaises(UnicodeError, codecs.encode, 'abc', 'undefined')
    CodecsModuleTest.assertRaises(UnicodeError, codecs.decode, b'abc', 'undefined')
    CodecsModuleTest.assertRaises(UnicodeError, codecs.encode, '', 'undefined')
    CodecsModuleTest.assertRaises(UnicodeError, codecs.decode, b'', 'undefined')
    for errors in ('strict', 'ignore', 'replace', 'backslashreplace'):
        CodecsModuleTest.assertRaises(UnicodeError, codecs.encode, 'abc', 'undefined', errors)
        CodecsModuleTest.assertRaises(UnicodeError, codecs.decode, b'abc', 'undefined', errors)

CodecsModuleTest = test_codecs.CodecsModuleTest()
test_undefined()
