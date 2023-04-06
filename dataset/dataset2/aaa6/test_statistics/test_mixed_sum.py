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

def test_mixed_sum():
    TestSum.assertRaises(TypeError, TestSum.func, [1, 2.0, Decimal(1)])
    TestSum.assertRaises(TypeError, TestSum.func, [1, 2.0], Decimal(1))

TestSum = test_statistics.TestSum()
TestSum.setUp()
test_mixed_sum()
