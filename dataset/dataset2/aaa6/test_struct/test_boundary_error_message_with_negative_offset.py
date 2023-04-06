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

def test_boundary_error_message_with_negative_offset():
    byte_list = bytearray(10)
    with StructTest.assertRaisesRegex(struct.error, 'no space to pack 4 bytes at offset -2'):
        struct.pack_into('<I', byte_list, -2, 123)
    with StructTest.assertRaisesRegex(struct.error, 'offset -11 out of range for 10-byte buffer'):
        struct.pack_into('<B', byte_list, -11, 123)
    with StructTest.assertRaisesRegex(struct.error, 'not enough data to unpack 4 bytes at offset -2'):
        struct.unpack_from('<I', byte_list, -2)
    with StructTest.assertRaisesRegex(struct.error, 'offset -11 out of range for 10-byte buffer'):
        struct.unpack_from('<B', byte_list, -11)

StructTest = test_struct.StructTest()
test_boundary_error_message_with_negative_offset()
