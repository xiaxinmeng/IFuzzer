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

def test_construct():

    def _check_iterator(it):
        UnpackIteratorTest.assertIsInstance(it, abc.Iterator)
        UnpackIteratorTest.assertIsInstance(it, abc.Iterable)
    s = struct.Struct('>ibcp')
    it = s.iter_unpack(b'')
    _check_iterator(it)
    it = s.iter_unpack(b'1234567')
    _check_iterator(it)
    with UnpackIteratorTest.assertRaises(struct.error):
        s.iter_unpack(b'123456')
    with UnpackIteratorTest.assertRaises(struct.error):
        s.iter_unpack(b'12345678')
    s = struct.Struct('>')
    with UnpackIteratorTest.assertRaises(struct.error):
        s.iter_unpack(b'')
    with UnpackIteratorTest.assertRaises(struct.error):
        s.iter_unpack(b'12')

UnpackIteratorTest = test_struct.UnpackIteratorTest()
test_construct()
