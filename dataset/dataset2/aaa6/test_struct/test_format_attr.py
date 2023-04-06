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

def test_format_attr():
    s = struct.Struct('=i2H')
    StructTest.assertEqual(s.format, '=i2H')
    s2 = struct.Struct(s.format.encode())
    StructTest.assertEqual(s2.format, s.format)

StructTest = test_struct.StructTest()
test_format_attr()
