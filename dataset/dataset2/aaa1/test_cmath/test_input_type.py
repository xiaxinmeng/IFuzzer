from test.support import requires_IEEE_754, cpython_only
from test.test_math import parse_testfile, test_file
import test.test_math as test_math
import unittest
import cmath, math
from cmath import phase, polar, rect, pi
import platform
import sys
from _testcapi import set_errno
import test_cmath

def test_input_type():
    for f in CMathTests.test_functions:
        for arg in [2, 2.0]:
            CMathTests.assertEqual(f(arg), f(arg.__float__()))
    for f in CMathTests.test_functions:
        for arg in ['a', 'long_string', '0', '1j', '']:
            CMathTests.assertRaises(TypeError, f, arg)

CMathTests = test_cmath.CMathTests()
test_input_type()
