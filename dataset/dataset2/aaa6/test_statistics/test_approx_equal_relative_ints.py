import bisect
import collections
import collections.abc
import copy
import decimal
import doctest
import math
import pickle
import random
import sys
import unittest
from test import support
from test.support import import_helper
from decimal import Decimal
from fractions import Fraction
import statistics
import test_statistics

def test_approx_equal_relative_ints():
    ApproxEqualInexactTest.assertTrue(test_statistics.approx_equal(64, 47, tol=0, rel=0.36))
    ApproxEqualInexactTest.assertTrue(test_statistics.approx_equal(64, 47, tol=0, rel=0.37))
    ApproxEqualInexactTest.assertTrue(test_statistics.approx_equal(449, 512, tol=0, rel=0.125))
    ApproxEqualInexactTest.assertTrue(test_statistics.approx_equal(448, 512, tol=0, rel=0.125))
    ApproxEqualInexactTest.assertFalse(test_statistics.approx_equal(447, 512, tol=0, rel=0.125))

ApproxEqualInexactTest = test_statistics.ApproxEqualInexactTest()
test_approx_equal_relative_ints()
