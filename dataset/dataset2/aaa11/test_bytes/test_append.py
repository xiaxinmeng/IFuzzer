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

def test_append():
    b = bytearray(b'hell')
    b.append(ord('o'))
    ByteArrayTest.assertEqual(b, b'hello')
    ByteArrayTest.assertEqual(b.append(100), None)
    b = bytearray()
    b.append(ord('A'))
    ByteArrayTest.assertEqual(len(b), 1)
    ByteArrayTest.assertRaises(TypeError, lambda : b.append(b'o'))
    b = bytearray()
    b.append(test_bytes.Indexable(ord('A')))
    ByteArrayTest.assertEqual(b, b'A')

ByteArrayTest = test_bytes.ByteArrayTest()
test_append()
