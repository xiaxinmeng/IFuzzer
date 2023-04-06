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

def test_open():
    CodecsModuleTest.addCleanup(os_helper.unlink, os_helper.TESTFN)
    for mode in ('w', 'r', 'r+', 'w+', 'a', 'a+'):
        with CodecsModuleTest.subTest(mode), codecs.open(os_helper.TESTFN, mode, 'ascii') as file:
            CodecsModuleTest.assertIsInstance(file, codecs.StreamReaderWriter)

CodecsModuleTest = test_codecs.CodecsModuleTest()
test_open()
