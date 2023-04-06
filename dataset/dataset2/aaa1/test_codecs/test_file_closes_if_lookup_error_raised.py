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

def test_file_closes_if_lookup_error_raised():
    mock_open = mock.mock_open()
    with mock.patch('builtins.open', mock_open) as file:
        with CodecsModuleTest.assertRaises(LookupError):
            codecs.open(os_helper.TESTFN, 'wt', 'invalid-encoding')
        file().close.assert_called()

CodecsModuleTest = test_codecs.CodecsModuleTest()
test_file_closes_if_lookup_error_raised()
