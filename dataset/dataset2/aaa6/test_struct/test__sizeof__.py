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

@support.cpython_only
def test__sizeof__():
    for code in test_struct.integer_codes:
        StructTest.check_sizeof(code, 1)
    StructTest.check_sizeof('BHILfdspP', 9)
    StructTest.check_sizeof('B' * 1234, 1234)
    StructTest.check_sizeof('fd', 2)
    StructTest.check_sizeof('xxxxxxxxxxxxxx', 0)
    StructTest.check_sizeof('100H', 1)
    StructTest.check_sizeof('187s', 1)
    StructTest.check_sizeof('20p', 1)
    StructTest.check_sizeof('0s', 1)
    StructTest.check_sizeof('0c', 0)

StructTest = test_struct.StructTest()
test__sizeof__()
