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

def test_exactly_equal_absolute():
    for n in [16, 1013, 1372, 1198, 971, 4]:
        ApproxEqualExactTest.do_exactly_equal_test(n, 0.01, 0)
        ApproxEqualExactTest.do_exactly_equal_test(n / 10, 0.01, 0)
        f = Fraction(n, 1234)
        ApproxEqualExactTest.do_exactly_equal_test(f, 0.01, 0)

ApproxEqualExactTest = test_statistics.ApproxEqualExactTest()
test_exactly_equal_absolute()
