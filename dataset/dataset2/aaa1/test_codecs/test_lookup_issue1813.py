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

def test_lookup_issue1813():
    oldlocale = locale.setlocale(locale.LC_CTYPE)
    CodecsModuleTest.addCleanup(locale.setlocale, locale.LC_CTYPE, oldlocale)
    try:
        locale.setlocale(locale.LC_CTYPE, 'tr_TR')
    except locale.Error:
        CodecsModuleTest.skipTest('test needs Turkish locale')
    c = codecs.lookup('ASCII')
    CodecsModuleTest.assertEqual(c.name, 'ascii')

CodecsModuleTest = test_codecs.CodecsModuleTest()
test_lookup_issue1813()
