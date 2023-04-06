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

def test_isbigendian():
    StructTest.assertEqual(struct.pack('=i', 1)[0] == 0, test_struct.ISBIGENDIAN)

StructTest = test_struct.StructTest()
test_isbigendian()
