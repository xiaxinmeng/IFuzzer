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

def test_issue35714():
    for s in ('\x00', '2\x00i', b'\x00'):
        with StructTest.assertRaisesRegex(struct.error, 'embedded null character'):
            struct.calcsize(s)

StructTest = test_struct.StructTest()
test_issue35714()
