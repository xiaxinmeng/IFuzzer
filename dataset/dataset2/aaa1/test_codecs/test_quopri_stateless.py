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

def test_quopri_stateless():
    encoded = codecs.encode(b'space tab\teol \n', 'quopri-codec')
    TransformCodecTest.assertEqual(encoded, b'space=20tab=09eol=20\n')
    unescaped = b'space tab eol\n'
    TransformCodecTest.assertEqual(codecs.decode(unescaped, 'quopri-codec'), unescaped)

TransformCodecTest = test_codecs.TransformCodecTest()
test_quopri_stateless()
