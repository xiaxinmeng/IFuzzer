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

def test_hex():
    BaseBytesTest.assertRaises(TypeError, BaseBytesTest.type2test.hex)
    BaseBytesTest.assertRaises(TypeError, BaseBytesTest.type2test.hex, 1)
    BaseBytesTest.assertEqual(BaseBytesTest.type2test(b'').hex(), '')
    BaseBytesTest.assertEqual(bytearray([26, 43, 48]).hex(), '1a2b30')
    BaseBytesTest.assertEqual(BaseBytesTest.type2test(b'\x1a+0').hex(), '1a2b30')
    BaseBytesTest.assertEqual(memoryview(b'\x1a+0').hex(), '1a2b30')

BaseBytesTest = test_bytes.BaseBytesTest()
test_hex()
