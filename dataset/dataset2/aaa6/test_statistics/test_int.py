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

def test_int():
    x = statistics._convert(Fraction(71), int)
    ExactRatioTest.check_exact_equal(x, 71)

    class MyInt(int):
        pass
    x = statistics._convert(Fraction(17), MyInt)
    ExactRatioTest.check_exact_equal(x, MyInt(17))

ExactRatioTest = test_statistics.ExactRatioTest()
ExactRatioTest.setUp()
test_int()
