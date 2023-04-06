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

def test_write():
    bio = io.BytesIO()
    codec = codecs.lookup('latin1')
    sr = codecs.StreamRecoder(bio, codec.encode, codec.decode, encodings.utf_8.StreamReader, encodings.utf_8.StreamWriter)
    text = 'àñé'
    sr.write(text.encode('latin1'))
    StreamRecoderTest.assertEqual(bio.getvalue(), text.encode('utf-8'))

StreamRecoderTest = test_codecs.StreamRecoderTest()
test_write()
