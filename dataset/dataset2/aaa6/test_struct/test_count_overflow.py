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

def test_count_overflow():
    hugecount = '{}b'.format(sys.maxsize + 1)
    StructTest.assertRaises(struct.error, struct.calcsize, hugecount)
    hugecount2 = '{}b{}H'.format(sys.maxsize // 2, sys.maxsize // 2)
    StructTest.assertRaises(struct.error, struct.calcsize, hugecount2)

StructTest = test_struct.StructTest()
test_count_overflow()
