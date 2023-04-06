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

def test_uninstantiable():
    iter_unpack_type = type(struct.Struct('>ibcp').iter_unpack(b''))
    UnpackIteratorTest.assertRaises(TypeError, iter_unpack_type)

UnpackIteratorTest = test_struct.UnpackIteratorTest()
test_uninstantiable()
