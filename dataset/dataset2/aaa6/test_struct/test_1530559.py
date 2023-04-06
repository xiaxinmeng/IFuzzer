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

def test_1530559():
    for (code, byteorder) in test_struct.iter_integer_formats():
        format = byteorder + code
        StructTest.assertRaises(struct.error, struct.pack, format, 1.0)
        StructTest.assertRaises(struct.error, struct.pack, format, 1.5)
    StructTest.assertRaises(struct.error, struct.pack, 'P', 1.0)
    StructTest.assertRaises(struct.error, struct.pack, 'P', 1.5)

StructTest = test_struct.StructTest()
test_1530559()
