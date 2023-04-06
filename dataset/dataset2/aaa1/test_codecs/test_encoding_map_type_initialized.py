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

def test_encoding_map_type_initialized():
    from encodings import cp1140
    table_type = type(cp1140.encoding_table)
    BasicUnicodeTest.assertEqual(table_type, table_type)

BasicUnicodeTest = test_codecs.BasicUnicodeTest()
test_encoding_map_type_initialized()
