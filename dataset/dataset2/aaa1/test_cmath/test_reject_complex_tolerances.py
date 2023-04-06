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

def test_reject_complex_tolerances():
    with IsCloseTests.assertRaises(TypeError):
        IsCloseTests.isclose(1j, 1j, rel_tol=1j)
    with IsCloseTests.assertRaises(TypeError):
        IsCloseTests.isclose(1j, 1j, abs_tol=1j)
    with IsCloseTests.assertRaises(TypeError):
        IsCloseTests.isclose(1j, 1j, rel_tol=1j, abs_tol=1j)

IsCloseTests = test_cmath.IsCloseTests()
test_reject_complex_tolerances()
