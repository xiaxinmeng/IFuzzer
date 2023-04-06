import dis
import math
import os
import unittest
import sys
import _ast
import tempfile
import types
from test import support
from test.support import script_helper
from test.support.os_helper import FakePath
import builtins

import dis, io
import test_compile

def test_unary_minus():
    if sys.maxsize == 2147483647:
        all_one_bits = '0xffffffff'
        TestSpecifics.assertEqual(eval(all_one_bits), 4294967295)
        TestSpecifics.assertEqual(eval('-' + all_one_bits), -4294967295)
    elif sys.maxsize == 9223372036854775807:
        all_one_bits = '0xffffffffffffffff'
        TestSpecifics.assertEqual(eval(all_one_bits), 18446744073709551615)
        TestSpecifics.assertEqual(eval('-' + all_one_bits), -18446744073709551615)
    else:
        TestSpecifics.fail('How many bits *does* this machine have???')
    TestSpecifics.assertIsInstance(eval('%s' % (-sys.maxsize - 1)), int)
    TestSpecifics.assertIsInstance(eval('%s' % (-sys.maxsize - 2)), int)

TestSpecifics = test_compile.TestSpecifics()
test_unary_minus()
