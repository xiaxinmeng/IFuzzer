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

def test_decimal():
    x = statistics._convert(Fraction(1, 40), Decimal)
    ExactRatioTest.check_exact_equal(x, Decimal('0.025'))

    class MyDecimal(Decimal):

        def __truediv__(ExactRatioTest, other):
            return ExactRatioTest.__class__(super().__truediv__(other))
    x = statistics._convert(Fraction(-15, 16), MyDecimal)
    ExactRatioTest.check_exact_equal(x, MyDecimal('-0.9375'))

ExactRatioTest = test_statistics.ExactRatioTest()
ExactRatioTest.setUp()
test_decimal()
