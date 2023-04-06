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

def test_trailing_counter():
    store = array.array('b', b' ' * 100)
    StructTest.assertRaises(struct.error, struct.pack, '12345')
    StructTest.assertRaises(struct.error, struct.unpack, '12345', b'')
    StructTest.assertRaises(struct.error, struct.pack_into, '12345', store, 0)
    StructTest.assertRaises(struct.error, struct.unpack_from, '12345', store, 0)
    StructTest.assertRaises(struct.error, struct.pack, 'c12345', 'x')
    StructTest.assertRaises(struct.error, struct.unpack, 'c12345', b'x')
    StructTest.assertRaises(struct.error, struct.pack_into, 'c12345', store, 0, 'x')
    StructTest.assertRaises(struct.error, struct.unpack_from, 'c12345', store, 0)
    StructTest.assertRaises(struct.error, struct.pack, '14s42', 'spam and eggs')
    StructTest.assertRaises(struct.error, struct.unpack, '14s42', b'spam and eggs')
    StructTest.assertRaises(struct.error, struct.pack_into, '14s42', store, 0, 'spam and eggs')
    StructTest.assertRaises(struct.error, struct.unpack_from, '14s42', store, 0)

StructTest = test_struct.StructTest()
test_trailing_counter()
