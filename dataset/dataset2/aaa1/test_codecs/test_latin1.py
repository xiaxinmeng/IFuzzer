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

def test_latin1():
    SurrogateEscapeTest.assertEqual('\udce4\udceb\udcef\udcf6\udcfc'.encode('latin-1', 'surrogateescape'), b'\xe4\xeb\xef\xf6\xfc')

SurrogateEscapeTest = test_codecs.SurrogateEscapeTest()
test_latin1()
