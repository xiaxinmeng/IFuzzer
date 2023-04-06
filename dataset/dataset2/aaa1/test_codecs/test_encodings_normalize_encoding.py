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

def test_encodings_normalize_encoding():
    normalize = encodings.normalize_encoding
    CodecNameNormalizationTest.assertEqual(normalize('utf_8'), 'utf_8')
    CodecNameNormalizationTest.assertEqual(normalize('utfé€\U0010ffff-8'), 'utf_8')
    CodecNameNormalizationTest.assertEqual(normalize('utf   8'), 'utf_8')
    CodecNameNormalizationTest.assertEqual(normalize('UTF 8'), 'UTF_8')
    CodecNameNormalizationTest.assertEqual(normalize('utf.8'), 'utf.8')
    CodecNameNormalizationTest.assertEqual(normalize('utf...8'), 'utf...8')

CodecNameNormalizationTest = test_codecs.CodecNameNormalizationTest()
test_encodings_normalize_encoding()
