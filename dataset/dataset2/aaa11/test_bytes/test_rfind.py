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

def test_rfind():
    b = BaseBytesTest.type2test(b'mississippi')
    i = 105
    w = 119
    BaseBytesTest.assertEqual(b.rfind(b'ss'), 5)
    BaseBytesTest.assertEqual(b.rfind(b'w'), -1)
    BaseBytesTest.assertEqual(b.rfind(b'mississippian'), -1)
    BaseBytesTest.assertEqual(b.rfind(i), 10)
    BaseBytesTest.assertEqual(b.rfind(w), -1)
    BaseBytesTest.assertEqual(b.rfind(b'ss', 3), 5)
    BaseBytesTest.assertEqual(b.rfind(b'ss', 0, 6), 2)
    BaseBytesTest.assertEqual(b.rfind(i, 1, 3), 1)
    BaseBytesTest.assertEqual(b.rfind(i, 3, 9), 7)
    BaseBytesTest.assertEqual(b.rfind(w, 1, 3), -1)

BaseBytesTest = test_bytes.BaseBytesTest()
test_rfind()
