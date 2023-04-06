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

def test_cp_utf7():
    cp = 65000
    CodePageTest.check_encode(cp, (('abc', 'strict', b'abc'), ('é€', 'strict', b'+AOkgrA-'), ('\U0010ffff', 'strict', b'+2//f/w-'), ('\udc80', 'strict', b'+3IA-'), ('�', 'strict', b'+//0-')))
    CodePageTest.check_decode(cp, ((b'abc', 'strict', 'abc'), (b'+AOkgrA-', 'strict', 'é€'), (b'+2//f/w-', 'strict', '\U0010ffff'), (b'+3IA-', 'strict', '\udc80'), (b'+//0-', 'strict', '�'), (b'[+/]', 'strict', '[]'), (b'[\xff]', 'strict', '[ÿ]')))

CodePageTest = test_codecs.CodePageTest()
test_cp_utf7()
