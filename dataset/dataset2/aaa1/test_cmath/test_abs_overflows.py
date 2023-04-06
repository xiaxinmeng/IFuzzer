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

@requires_IEEE_754
def test_abs_overflows():
    CMathTests.assertRaises(OverflowError, abs, complex(1.4e+308, 1.4e+308))

CMathTests = test_cmath.CMathTests()
test_abs_overflows()
