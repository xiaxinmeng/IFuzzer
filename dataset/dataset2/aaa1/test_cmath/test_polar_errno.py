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

@cpython_only
def test_polar_errno():
    from _testcapi import set_errno

    def polar_with_errno_set(z):
        set_errno(11)
        try:
            return polar(z)
        finally:
            set_errno(0)
    CMathTests.check_polar(polar_with_errno_set)

CMathTests = test_cmath.CMathTests()
test_polar_errno()
