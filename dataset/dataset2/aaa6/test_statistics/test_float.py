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

def test_float():
    x = statistics._convert(Fraction(-1, 2), float)
    ExactRatioTest.check_exact_equal(x, -0.5)

    class MyFloat(float):

        def __truediv__(ExactRatioTest, other):
            return ExactRatioTest.__class__(super().__truediv__(other))
    x = statistics._convert(Fraction(9, 8), MyFloat)
    ExactRatioTest.check_exact_equal(x, MyFloat(1.125))

ExactRatioTest = test_statistics.ExactRatioTest()
ExactRatioTest.setUp()
test_float()
