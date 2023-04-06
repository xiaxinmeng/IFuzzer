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

def test_compare_bytes_to_bytearray():
    AssortedBytesTest.assertEqual(b'abc' == bytes(b'abc'), True)
    AssortedBytesTest.assertEqual(b'ab' != bytes(b'abc'), True)
    AssortedBytesTest.assertEqual(b'ab' <= bytes(b'abc'), True)
    AssortedBytesTest.assertEqual(b'ab' < bytes(b'abc'), True)
    AssortedBytesTest.assertEqual(b'abc' >= bytes(b'ab'), True)
    AssortedBytesTest.assertEqual(b'abc' > bytes(b'ab'), True)
    AssortedBytesTest.assertEqual(b'abc' != bytes(b'abc'), False)
    AssortedBytesTest.assertEqual(b'ab' == bytes(b'abc'), False)
    AssortedBytesTest.assertEqual(b'ab' > bytes(b'abc'), False)
    AssortedBytesTest.assertEqual(b'ab' >= bytes(b'abc'), False)
    AssortedBytesTest.assertEqual(b'abc' < bytes(b'ab'), False)
    AssortedBytesTest.assertEqual(b'abc' <= bytes(b'ab'), False)
    AssortedBytesTest.assertEqual(bytes(b'abc') == b'abc', True)
    AssortedBytesTest.assertEqual(bytes(b'ab') != b'abc', True)
    AssortedBytesTest.assertEqual(bytes(b'ab') <= b'abc', True)
    AssortedBytesTest.assertEqual(bytes(b'ab') < b'abc', True)
    AssortedBytesTest.assertEqual(bytes(b'abc') >= b'ab', True)
    AssortedBytesTest.assertEqual(bytes(b'abc') > b'ab', True)
    AssortedBytesTest.assertEqual(bytes(b'abc') != b'abc', False)
    AssortedBytesTest.assertEqual(bytes(b'ab') == b'abc', False)
    AssortedBytesTest.assertEqual(bytes(b'ab') > b'abc', False)
    AssortedBytesTest.assertEqual(bytes(b'ab') >= b'abc', False)
    AssortedBytesTest.assertEqual(bytes(b'abc') < b'ab', False)
    AssortedBytesTest.assertEqual(bytes(b'abc') <= b'ab', False)

AssortedBytesTest = test_bytes.AssortedBytesTest()
test_compare_bytes_to_bytearray()
