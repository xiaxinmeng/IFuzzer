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

def test_lone_surrogates():
    tests = [(b'a+2AE-b', 'a\ud801b'), (b'a+2AE\xffb', 'a�b'), (b'a+2AE', 'a�'), (b'a+2AEA-b', 'a�b'), (b'a+2AH-b', 'a�b'), (b'a+IKzYAQ-b', 'a€\ud801b'), (b'a+IKzYAQ\xffb', 'a€�b'), (b'a+IKzYAQA-b', 'a€�b'), (b'a+IKzYAd-b', 'a€�b'), (b'a+IKwgrNgB-b', 'a€€\ud801b'), (b'a+IKwgrNgB\xffb', 'a€€�b'), (b'a+IKwgrNgB', 'a€€�'), (b'a+IKwgrNgBA-b', 'a€€�b')]
    for (raw, expected) in tests:
        with ReadTest.subTest(raw=raw):
            ReadTest.assertEqual(raw.decode('utf-7', 'replace'), expected)

ReadTest = test_codecs.ReadTest()
test_lone_surrogates()
