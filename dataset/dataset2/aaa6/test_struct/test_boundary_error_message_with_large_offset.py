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

def test_boundary_error_message_with_large_offset():
    regex1 = 'pack_into requires a buffer of at least ' + str(sys.maxsize + 4) + ' bytes for packing 4 bytes at offset ' + str(sys.maxsize) + ' \\(actual buffer size is 10\\)'
    with StructTest.assertRaisesRegex(struct.error, regex1):
        struct.pack_into('<I', bytearray(10), sys.maxsize, 1)
    regex2 = 'unpack_from requires a buffer of at least ' + str(sys.maxsize + 4) + ' bytes for unpacking 4 bytes at offset ' + str(sys.maxsize) + ' \\(actual buffer size is 10\\)'
    with StructTest.assertRaisesRegex(struct.error, regex2):
        struct.unpack_from('<I', bytearray(10), sys.maxsize)

StructTest = test_struct.StructTest()
test_boundary_error_message_with_large_offset()
