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

@test.support.requires_docstrings
def test_doc():
    AssortedBytesTest.assertIsNotNone(bytearray.__doc__)
    AssortedBytesTest.assertTrue(bytearray.__doc__.startswith('bytearray('), bytearray.__doc__)
    AssortedBytesTest.assertIsNotNone(bytes.__doc__)
    AssortedBytesTest.assertTrue(bytes.__doc__.startswith('bytes('), bytes.__doc__)

AssortedBytesTest = test_bytes.AssortedBytesTest()
test_doc()