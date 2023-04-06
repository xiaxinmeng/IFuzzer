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

def test_infinity_and_nan_constants():
    CMathTests.assertEqual(cmath.inf.real, math.inf)
    CMathTests.assertEqual(cmath.inf.imag, 0.0)
    CMathTests.assertEqual(cmath.infj.real, 0.0)
    CMathTests.assertEqual(cmath.infj.imag, math.inf)
    CMathTests.assertTrue(math.isnan(cmath.nan.real))
    CMathTests.assertEqual(cmath.nan.imag, 0.0)
    CMathTests.assertEqual(cmath.nanj.real, 0.0)
    CMathTests.assertTrue(math.isnan(cmath.nanj.imag))
    CMathTests.assertEqual(repr(cmath.inf), 'inf')
    CMathTests.assertEqual(repr(cmath.infj), 'infj')
    CMathTests.assertEqual(repr(cmath.nan), 'nan')
    CMathTests.assertEqual(repr(cmath.nanj), 'nanj')

CMathTests = test_cmath.CMathTests()
test_infinity_and_nan_constants()
