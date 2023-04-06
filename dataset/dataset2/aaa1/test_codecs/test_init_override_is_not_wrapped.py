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

def test_init_override_is_not_wrapped():

    class CustomInit(RuntimeError):

        def __init__(ExceptionChainingTest):
            pass
    ExceptionChainingTest.check_not_wrapped(CustomInit, '')

ExceptionChainingTest = test_codecs.ExceptionChainingTest()
test_init_override_is_not_wrapped()
