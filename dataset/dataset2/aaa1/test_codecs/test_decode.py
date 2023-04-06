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

def test_decode():
    plaintext = codecs.decode('Rg gh, Oehgr?', 'rot-13')
    PunycodeTest.assertEqual(plaintext, 'Et tu, Brute?')

PunycodeTest = test_codecs.PunycodeTest()
test_decode()
