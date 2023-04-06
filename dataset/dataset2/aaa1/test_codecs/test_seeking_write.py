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

def test_seeking_write():
    bio = io.BytesIO('123456789\n'.encode('utf-16-le'))
    sr = codecs.EncodedFile(bio, 'utf-8', 'utf-16-le')
    sr.seek(2)
    sr.write(b'\nabc\n')
    StreamRecoderTest.assertEqual(sr.readline(), b'789\n')
    sr.seek(0)
    StreamRecoderTest.assertEqual(sr.readline(), b'1\n')
    StreamRecoderTest.assertEqual(sr.readline(), b'abc\n')
    StreamRecoderTest.assertEqual(sr.readline(), b'789\n')

StreamRecoderTest = test_codecs.StreamRecoderTest()
test_seeking_write()
