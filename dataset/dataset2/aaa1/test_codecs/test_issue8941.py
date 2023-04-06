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

def test_issue8941():
    encoded = b'\x00\x01\x00\x00' * 1024
    UTF32Test.assertEqual('𐀀' * 1024, codecs.utf_32_be_decode(encoded)[0])

UTF32Test = test_codecs.UTF32Test()
test_issue8941()
