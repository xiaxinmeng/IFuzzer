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

@test_bytes.check_bytes_warnings
def test_to_str():
    AssortedBytesTest.assertEqual(str(b''), "b''")
    AssortedBytesTest.assertEqual(str(b'x'), "b'x'")
    AssortedBytesTest.assertEqual(str(b'\x80'), "b'\\x80'")
    AssortedBytesTest.assertEqual(str(bytearray(b'')), "bytearray(b'')")
    AssortedBytesTest.assertEqual(str(bytearray(b'x')), "bytearray(b'x')")
    AssortedBytesTest.assertEqual(str(bytearray(b'\x80')), "bytearray(b'\\x80')")

AssortedBytesTest = test_bytes.AssortedBytesTest()
test_to_str()
