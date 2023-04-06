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

def test_constructor_value_errors():
    BaseBytesTest.assertRaises(ValueError, BaseBytesTest.type2test, [-1])
    BaseBytesTest.assertRaises(ValueError, BaseBytesTest.type2test, [-sys.maxsize])
    BaseBytesTest.assertRaises(ValueError, BaseBytesTest.type2test, [-sys.maxsize - 1])
    BaseBytesTest.assertRaises(ValueError, BaseBytesTest.type2test, [-sys.maxsize - 2])
    BaseBytesTest.assertRaises(ValueError, BaseBytesTest.type2test, [-10 ** 100])
    BaseBytesTest.assertRaises(ValueError, BaseBytesTest.type2test, [256])
    BaseBytesTest.assertRaises(ValueError, BaseBytesTest.type2test, [257])
    BaseBytesTest.assertRaises(ValueError, BaseBytesTest.type2test, [sys.maxsize])
    BaseBytesTest.assertRaises(ValueError, BaseBytesTest.type2test, [sys.maxsize + 1])
    BaseBytesTest.assertRaises(ValueError, BaseBytesTest.type2test, [10 ** 100])

BaseBytesTest = test_bytes.BaseBytesTest()
test_constructor_value_errors()
