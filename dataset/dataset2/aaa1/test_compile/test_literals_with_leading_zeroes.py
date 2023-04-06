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

def test_literals_with_leading_zeroes():
    for arg in ['077787', '0xj', '0x.', '0e', '090000000000000', '080000000000000', '000000000000009', '000000000000008', '0b42', '0BADCAFE', '0o123456789', '0b1.1', '0o4.2', '0b101j2', '0o153j2', '0b100e1', '0o777e1', '0777', '000777', '000000000000007']:
        TestSpecifics.assertRaises(SyntaxError, eval, arg)
    TestSpecifics.assertEqual(eval('0xff'), 255)
    TestSpecifics.assertEqual(eval('0777.'), 777)
    TestSpecifics.assertEqual(eval('0777.0'), 777)
    TestSpecifics.assertEqual(eval('000000000000000000000000000000000000000000000000000777e0'), 777)
    TestSpecifics.assertEqual(eval('0777e1'), 7770)
    TestSpecifics.assertEqual(eval('0e0'), 0)
    TestSpecifics.assertEqual(eval('0000e-012'), 0)
    TestSpecifics.assertEqual(eval('09.5'), 9.5)
    TestSpecifics.assertEqual(eval('0777j'), 777j)
    TestSpecifics.assertEqual(eval('000'), 0)
    TestSpecifics.assertEqual(eval('00j'), 0j)
    TestSpecifics.assertEqual(eval('00.0'), 0)
    TestSpecifics.assertEqual(eval('0e3'), 0)
    TestSpecifics.assertEqual(eval('090000000000000.'), 90000000000000.0)
    TestSpecifics.assertEqual(eval('090000000000000.0000000000000000000000'), 90000000000000.0)
    TestSpecifics.assertEqual(eval('090000000000000e0'), 90000000000000.0)
    TestSpecifics.assertEqual(eval('090000000000000e-0'), 90000000000000.0)
    TestSpecifics.assertEqual(eval('090000000000000j'), 90000000000000j)
    TestSpecifics.assertEqual(eval('000000000000008.'), 8.0)
    TestSpecifics.assertEqual(eval('000000000000009.'), 9.0)
    TestSpecifics.assertEqual(eval('0b101010'), 42)
    TestSpecifics.assertEqual(eval('-0b000000000010'), -2)
    TestSpecifics.assertEqual(eval('0o777'), 511)
    TestSpecifics.assertEqual(eval('-0o0000010'), -8)

TestSpecifics = test_compile.TestSpecifics()
test_literals_with_leading_zeroes()
