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

def test_order_doesnt_matter():
    data = [1, 2, 3, 3, 3, 4, 5, 6] * 100
    expected = UnivariateCommonMixin.func(data)
    random.shuffle(data)
    actual = UnivariateCommonMixin.func(data)
    UnivariateCommonMixin.assertEqual(expected, actual)

UnivariateCommonMixin = test_statistics.UnivariateCommonMixin()
test_order_doesnt_matter()
