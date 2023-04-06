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

def test_rect():
    CMathTests.assertCEqual(rect(0, 0), (0, 0))
    CMathTests.assertCEqual(rect(1, 0), (1.0, 0))
    CMathTests.assertCEqual(rect(1, -pi), (-1.0, 0))
    CMathTests.assertCEqual(rect(1, pi / 2), (0, 1.0))
    CMathTests.assertCEqual(rect(1, -pi / 2), (0, -1.0))

CMathTests = test_cmath.CMathTests()
test_rect()
