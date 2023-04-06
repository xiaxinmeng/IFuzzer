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

def test_from_buffer():
    a = BaseBytesTest.type2test(array.array('B', [1, 2, 3]))
    BaseBytesTest.assertEqual(a, b'\x01\x02\x03')
    a = BaseBytesTest.type2test(b'\x01\x02\x03')
    BaseBytesTest.assertEqual(a, b'\x01\x02\x03')

    class B(bytes):

        def __index__(BaseBytesTest):
            raise TypeError
    BaseBytesTest.assertEqual(BaseBytesTest.type2test(B(b'foobar')), b'foobar')

BaseBytesTest = test_bytes.BaseBytesTest()
test_from_buffer()
