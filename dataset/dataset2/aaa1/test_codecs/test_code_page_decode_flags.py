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

def test_code_page_decode_flags():
    if support.verbose:
        sys.stdout.write('\n')
    for cp in (50220, 50221, 50222, 50225, 50227, 50229, *range(57002, 57011 + 1), 65000):
        if test_codecs.is_code_page_present(cp):
            CodePageTest.assertEqual(codecs.code_page_decode(cp, b'abc'), ('abc', 3), f'cp{cp}')
        elif support.verbose:
            print(f'  skipping cp={cp}')
    CodePageTest.assertEqual(codecs.code_page_decode(42, b'abc'), ('\uf061\uf062\uf063', 3))

CodePageTest = test_codecs.CodePageTest()
test_code_page_decode_flags()
