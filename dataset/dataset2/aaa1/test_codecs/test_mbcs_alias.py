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

def test_mbcs_alias():
    with mock.patch('_winapi.GetACP', return_value=123):
        codec = codecs.lookup('cp123')
        CodePageTest.assertEqual(codec.name, 'mbcs')

CodePageTest = test_codecs.CodePageTest()
test_mbcs_alias()
