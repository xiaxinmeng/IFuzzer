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

def test_seeking_read():
    bio = io.BytesIO('line1\nline2\nline3\n'.encode('utf-16-le'))
    sr = codecs.EncodedFile(bio, 'utf-8', 'utf-16-le')
    StreamRecoderTest.assertEqual(sr.readline(), b'line1\n')
    sr.seek(0)
    StreamRecoderTest.assertEqual(sr.readline(), b'line1\n')
    StreamRecoderTest.assertEqual(sr.readline(), b'line2\n')
    StreamRecoderTest.assertEqual(sr.readline(), b'line3\n')
    StreamRecoderTest.assertEqual(sr.readline(), b'')

StreamRecoderTest = test_codecs.StreamRecoderTest()
test_seeking_read()
