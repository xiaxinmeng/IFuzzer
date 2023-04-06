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

def test_multiple_args_is_not_wrapped():
    msg_re = "^\\('a', 'b', 'c'\\)$"
    ExceptionChainingTest.check_not_wrapped(RuntimeError('a', 'b', 'c'), msg_re)

ExceptionChainingTest = test_codecs.ExceptionChainingTest()
test_multiple_args_is_not_wrapped()
