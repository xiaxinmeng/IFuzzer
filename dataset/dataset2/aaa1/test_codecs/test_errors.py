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

def test_errors():
    """Only supports "strict" error handler"""
    'python.org'.encode('idna', 'strict')
    b'python.org'.decode('idna', 'strict')
    for errors in ('ignore', 'replace', 'backslashreplace', 'surrogateescape'):
        UTF32Test.assertRaises(Exception, 'python.org'.encode, 'idna', errors)
        UTF32Test.assertRaises(Exception, b'python.org'.decode, 'idna', errors)

UTF32Test = test_codecs.UTF32Test()
test_errors()
