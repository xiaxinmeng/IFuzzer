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

def test_struct_cleans_up_at_runtime_shutdown():
    code = "if 1:\n            import struct\n\n            class C:\n                def __init__(StructTest):\n                    StructTest.pack = struct.pack\n                def __del__(StructTest):\n                    StructTest.pack('I', -42)\n\n            struct.x = C()\n            "
    (rc, stdout, stderr) = assert_python_ok('-c', code)
    StructTest.assertEqual(rc, 0)
    StructTest.assertEqual(stdout.rstrip(), b'')
    StructTest.assertIn(b'Exception ignored in:', stderr)
    StructTest.assertIn(b'C.__del__', stderr)

StructTest = test_struct.StructTest()
test_struct_cleans_up_at_runtime_shutdown()
