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

def test_hex_separator_six_bytes():
    six_bytes = BaseBytesTest.type2test((x * 3 for x in range(1, 7)))
    BaseBytesTest.assertEqual(six_bytes.hex(), '0306090c0f12')
    BaseBytesTest.assertEqual(six_bytes.hex('.', 1), '03.06.09.0c.0f.12')
    BaseBytesTest.assertEqual(six_bytes.hex(' ', 2), '0306 090c 0f12')
    BaseBytesTest.assertEqual(six_bytes.hex('-', 3), '030609-0c0f12')
    BaseBytesTest.assertEqual(six_bytes.hex(':', 4), '0306:090c0f12')
    BaseBytesTest.assertEqual(six_bytes.hex(':', 5), '03:06090c0f12')
    BaseBytesTest.assertEqual(six_bytes.hex(':', 6), '0306090c0f12')
    BaseBytesTest.assertEqual(six_bytes.hex(':', 95), '0306090c0f12')
    BaseBytesTest.assertEqual(six_bytes.hex('_', -3), '030609_0c0f12')
    BaseBytesTest.assertEqual(six_bytes.hex(':', -4), '0306090c:0f12')
    BaseBytesTest.assertEqual(six_bytes.hex(b'@', -5), '0306090c0f@12')
    BaseBytesTest.assertEqual(six_bytes.hex(':', -6), '0306090c0f12')
    BaseBytesTest.assertEqual(six_bytes.hex(' ', -95), '0306090c0f12')

BaseBytesTest = test_bytes.BaseBytesTest()
test_hex_separator_six_bytes()
