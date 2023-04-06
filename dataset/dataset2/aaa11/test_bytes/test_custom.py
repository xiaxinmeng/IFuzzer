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

def test_custom():

    class A:

        def __bytes__(BytesTest):
            return b'abc'
    BytesTest.assertEqual(bytes(A()), b'abc')

    class A:
        pass
    BytesTest.assertRaises(TypeError, bytes, A())

    class A:

        def __bytes__(BytesTest):
            return None
    BytesTest.assertRaises(TypeError, bytes, A())

    class A:

        def __bytes__(BytesTest):
            return b'a'

        def __index__(BytesTest):
            return 42
    BytesTest.assertEqual(bytes(A()), b'a')

    class A(str):

        def __bytes__(BytesTest):
            return b'abc'
    BytesTest.assertEqual(bytes(A('€')), b'abc')
    BytesTest.assertEqual(bytes(A('€'), 'iso8859-15'), b'\xa4')

    class A:

        def __bytes__(BytesTest):
            return test_bytes.OtherBytesSubclass(b'abc')
    BytesTest.assertEqual(bytes(A()), b'abc')
    BytesTest.assertIs(type(bytes(A())), test_bytes.OtherBytesSubclass)
    BytesTest.assertEqual(test_bytes.BytesSubclass(A()), b'abc')
    BytesTest.assertIs(type(test_bytes.BytesSubclass(A())), test_bytes.BytesSubclass)

BytesTest = test_bytes.BytesTest()
test_custom()
