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

def test_new_override_is_not_wrapped():

    class CustomNew(RuntimeError):

        def __new__(cls):
            return super().__new__(cls)
    ExceptionChainingTest.check_not_wrapped(CustomNew, '')

ExceptionChainingTest = test_codecs.ExceptionChainingTest()
test_new_override_is_not_wrapped()
