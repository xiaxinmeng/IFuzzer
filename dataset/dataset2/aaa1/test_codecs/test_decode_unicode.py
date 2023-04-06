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

def test_decode_unicode():
    decoders = [codecs.utf_7_decode, codecs.utf_8_decode, codecs.utf_16_le_decode, codecs.utf_16_be_decode, codecs.utf_16_ex_decode, codecs.utf_32_decode, codecs.utf_32_le_decode, codecs.utf_32_be_decode, codecs.utf_32_ex_decode, codecs.latin_1_decode, codecs.ascii_decode, codecs.charmap_decode]
    if hasattr(codecs, 'mbcs_decode'):
        decoders.append(codecs.mbcs_decode)
    for decoder in decoders:
        TypesTest.assertRaises(TypeError, decoder, 'xxx')

TypesTest = test_codecs.TypesTest()
test_decode_unicode()
