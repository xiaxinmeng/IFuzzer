import array
import os
import re
import sys
import copy
import functools
import pickle
import tempfile
import textwrap
import unittest
import test.support
from test.support import import_helper
from test.support import warnings_helper
import test.string_tests
import test.list_tests
from test.support import bigaddrspacetest, MAX_Py_ssize_t
from test.support.script_helper import assert_python_failure
from ctypes import pythonapi, py_object
from ctypes import c_int, c_uint, c_long, c_ulong, c_size_t, c_ssize_t, c_char_p
from _testcapi import getbuffer_with_null_view
import test_bytes

def test_from_mutating_list():

    class X:

        def __index__(BaseBytesTest):
            a.clear()
            return 42
    a = [X(), X()]
    BaseBytesTest.assertEqual(bytes(a), b'*')

    class Y:

        def __index__(BaseBytesTest):
            if len(a) < 1000:
                a.append(BaseBytesTest)
            return 42
    a = [Y()]
    BaseBytesTest.assertEqual(bytes(a), b'*' * 1000)

BaseBytesTest = test_bytes.BaseBytesTest()
test_from_mutating_list()
