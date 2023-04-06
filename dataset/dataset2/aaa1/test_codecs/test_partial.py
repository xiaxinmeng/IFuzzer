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

def test_partial():
    UTF32Test.check_partial('\ufeff\x00ÿ߿ࠀ\uffff𐀀', ['', '', '', '', '', '\ufeff', '\ufeff\x00', '\ufeff\x00', '\ufeff\x00ÿ', '\ufeff\x00ÿ', '\ufeff\x00ÿ߿', '\ufeff\x00ÿ߿', '\ufeff\x00ÿ߿', '\ufeff\x00ÿ߿ࠀ', '\ufeff\x00ÿ߿ࠀ', '\ufeff\x00ÿ߿ࠀ', '\ufeff\x00ÿ߿ࠀ\uffff', '\ufeff\x00ÿ߿ࠀ\uffff', '\ufeff\x00ÿ߿ࠀ\uffff', '\ufeff\x00ÿ߿ࠀ\uffff', '\ufeff\x00ÿ߿ࠀ\uffff𐀀'])

UTF32Test = test_codecs.UTF32Test()
test_partial()
