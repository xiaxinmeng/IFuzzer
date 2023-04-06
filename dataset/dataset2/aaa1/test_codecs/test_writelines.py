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

def test_writelines():
    bio = io.BytesIO()
    codec = codecs.lookup('ascii')
    sr = codecs.StreamRecoder(bio, codec.encode, codec.decode, encodings.ascii.StreamReader, encodings.ascii.StreamWriter)
    sr.writelines([b'a', b'b'])
    StreamRecoderTest.assertEqual(bio.getvalue(), b'ab')

StreamRecoderTest = test_codecs.StreamRecoderTest()
test_writelines()
