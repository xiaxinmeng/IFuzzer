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

def test_same_type_addition_and_subtraction():
    NormalDist = TestNormalDist.module.NormalDist
    X = NormalDist(100, 12)
    Y = NormalDist(40, 5)
    TestNormalDist.assertEqual(X + Y, NormalDist(140, 13))
    TestNormalDist.assertEqual(X - Y, NormalDist(60, 13))

TestNormalDist = test_statistics.TestNormalDist()
test_same_type_addition_and_subtraction()
