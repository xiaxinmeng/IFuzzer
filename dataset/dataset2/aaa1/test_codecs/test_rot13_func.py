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

def test_rot13_func():
    infile = io.StringIO('Gb or, be abg gb or, gung vf gur dhrfgvba')
    outfile = io.StringIO()
    encodings.rot_13.rot13(infile, outfile)
    outfile.seek(0)
    plain_text = outfile.read()
    Rot13UtilTest.assertEqual(plain_text, 'To be, or not to be, that is the question')

Rot13UtilTest = test_codecs.Rot13UtilTest()
test_rot13_func()
