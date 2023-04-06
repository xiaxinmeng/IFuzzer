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

def test_constants():
    e_expected = 2.718281828459045
    pi_expected = 3.141592653589793
    CMathTests.assertAlmostEqual(cmath.pi, pi_expected, places=9, msg='cmath.pi is {}; should be {}'.format(cmath.pi, pi_expected))
    CMathTests.assertAlmostEqual(cmath.e, e_expected, places=9, msg='cmath.e is {}; should be {}'.format(cmath.e, e_expected))

CMathTests = test_cmath.CMathTests()
test_constants()
