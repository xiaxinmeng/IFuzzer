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

def test_complex_near_zero():
    near_zero_examples = [(0.001j, 0), (0.001, 0), (0.001 + 0.001j, 0), (-0.001 + 0.001j, 0), (0.001 - 0.001j, 0), (-0.001 - 0.001j, 0)]
    IsCloseTests.assertAllClose(near_zero_examples, abs_tol=0.0015)
    IsCloseTests.assertAllNotClose(near_zero_examples, abs_tol=0.0005)
    IsCloseTests.assertIsClose(0.001 - 0.001j, 0.001 + 0.001j, abs_tol=0.002)
    IsCloseTests.assertIsNotClose(0.001 - 0.001j, 0.001 + 0.001j, abs_tol=0.001)

IsCloseTests = test_cmath.IsCloseTests()
test_complex_near_zero()
