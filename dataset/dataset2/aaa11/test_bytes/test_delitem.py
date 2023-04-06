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

def test_delitem():
    b = bytearray(range(10))
    del b[0]
    ByteArrayTest.assertEqual(b, bytearray(range(1, 10)))
    del b[-1]
    ByteArrayTest.assertEqual(b, bytearray(range(1, 9)))
    del b[4]
    ByteArrayTest.assertEqual(b, bytearray([1, 2, 3, 4, 6, 7, 8]))

ByteArrayTest = test_bytes.ByteArrayTest()
test_delitem()
