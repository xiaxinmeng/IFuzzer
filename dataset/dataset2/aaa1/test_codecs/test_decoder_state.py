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

def test_decoder_state():
    u = 'abc123'
    for encoding in test_codecs.all_unicode_encodings:
        if encoding not in test_codecs.broken_unicode_with_stateful:
            UTF32Test.check_state_handling_decode(encoding, u, u.encode(encoding))
            UTF32Test.check_state_handling_encode(encoding, u, u.encode(encoding))

UTF32Test = test_codecs.UTF32Test()
test_decoder_state()
