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

def test_non_str_arg_is_not_wrapped():
    ExceptionChainingTest.check_not_wrapped(RuntimeError(1), '1')

ExceptionChainingTest = test_codecs.ExceptionChainingTest()
test_non_str_arg_is_not_wrapped()
