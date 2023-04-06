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

def test_nonbmp():
    UTF16LETest.assertEqual('𐒠'.encode(UTF16LETest.encoding), b'+2AHcoA-')
    UTF16LETest.assertEqual('\ud801\udca0'.encode(UTF16LETest.encoding), b'+2AHcoA-')
    UTF16LETest.assertEqual(b'+2AHcoA-'.decode(UTF16LETest.encoding), '𐒠')
    UTF16LETest.assertEqual(b'+2AHcoA'.decode(UTF16LETest.encoding), '𐒠')
    UTF16LETest.assertEqual('€𐒠'.encode(UTF16LETest.encoding), b'+IKzYAdyg-')
    UTF16LETest.assertEqual(b'+IKzYAdyg-'.decode(UTF16LETest.encoding), '€𐒠')
    UTF16LETest.assertEqual(b'+IKzYAdyg'.decode(UTF16LETest.encoding), '€𐒠')
    UTF16LETest.assertEqual('€€𐒠'.encode(UTF16LETest.encoding), b'+IKwgrNgB3KA-')
    UTF16LETest.assertEqual(b'+IKwgrNgB3KA-'.decode(UTF16LETest.encoding), '€€𐒠')
    UTF16LETest.assertEqual(b'+IKwgrNgB3KA'.decode(UTF16LETest.encoding), '€€𐒠')

UTF16LETest = test_codecs.UTF16LETest()
test_nonbmp()
