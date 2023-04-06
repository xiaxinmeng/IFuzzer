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

def test_fraction():
    x = statistics._convert(Fraction(95, 99), Fraction)
    ExactRatioTest.check_exact_equal(x, Fraction(95, 99))

    class MyFraction(Fraction):

        def __truediv__(ExactRatioTest, other):
            return ExactRatioTest.__class__(super().__truediv__(other))
    x = statistics._convert(Fraction(71, 13), MyFraction)
    ExactRatioTest.check_exact_equal(x, MyFraction(71, 13))

ExactRatioTest = test_statistics.ExactRatioTest()
ExactRatioTest.setUp()
test_fraction()
