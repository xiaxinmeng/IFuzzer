from collections import abc
import array
import math
import operator
import unittest
import struct
import sys
from test import support
from test.support.script_helper import assert_python_ok
import binascii
from random import randrange
import test_struct

def test_boundary_error_message():
    regex1 = 'pack_into requires a buffer of at least 6 bytes for packing 1 bytes at offset 5 \\(actual buffer size is 1\\)'
    with StructTest.assertRaisesRegex(struct.error, regex1):
        struct.pack_into('b', bytearray(1), 5, 1)
    regex2 = 'unpack_from requires a buffer of at least 6 bytes for unpacking 1 bytes at offset 5 \\(actual buffer size is 1\\)'
    with StructTest.assertRaisesRegex(struct.error, regex2):
        struct.unpack_from('b', bytearray(1), 5)

StructTest = test_struct.StructTest()
test_boundary_error_message()
