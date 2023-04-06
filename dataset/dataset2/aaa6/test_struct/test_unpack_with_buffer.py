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

def test_unpack_with_buffer():
    data1 = array.array('B', b'\x124Vx')
    data2 = memoryview(b'\x124Vx')
    for data in [data1, data2]:
        (value,) = struct.unpack('>I', data)
        StructTest.assertEqual(value, 305419896)

StructTest = test_struct.StructTest()
test_unpack_with_buffer()
