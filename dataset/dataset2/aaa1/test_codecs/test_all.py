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

def test_all():
    api = ('encode', 'decode', 'register', 'CodecInfo', 'Codec', 'IncrementalEncoder', 'IncrementalDecoder', 'StreamReader', 'StreamWriter', 'lookup', 'getencoder', 'getdecoder', 'getincrementalencoder', 'getincrementaldecoder', 'getreader', 'getwriter', 'register_error', 'lookup_error', 'strict_errors', 'replace_errors', 'ignore_errors', 'xmlcharrefreplace_errors', 'backslashreplace_errors', 'namereplace_errors', 'open', 'EncodedFile', 'iterencode', 'iterdecode', 'BOM', 'BOM_BE', 'BOM_LE', 'BOM_UTF8', 'BOM_UTF16', 'BOM_UTF16_BE', 'BOM_UTF16_LE', 'BOM_UTF32', 'BOM_UTF32_BE', 'BOM_UTF32_LE', 'BOM32_BE', 'BOM32_LE', 'BOM64_BE', 'BOM64_LE', 'StreamReaderWriter', 'StreamRecoder')
    CodecsModuleTest.assertCountEqual(api, codecs.__all__)
    for api in codecs.__all__:
        getattr(codecs, api)

CodecsModuleTest = test_codecs.CodecsModuleTest()
test_all()
