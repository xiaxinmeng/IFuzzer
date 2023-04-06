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

def test_complex_values():
    complex_examples = [(1.0 + 1j, 1.000000000001 + 1j), (1.0 + 1j, 1.0 + 1.000000000001j), (-1.0 + 1j, -1.000000000001 + 1j), (1.0 - 1j, 1.0 - 0.999999999999j)]
    IsCloseTests.assertAllClose(complex_examples, rel_tol=1e-12)
    IsCloseTests.assertAllNotClose(complex_examples, rel_tol=1e-13)

IsCloseTests = test_cmath.IsCloseTests()
test_complex_values()
