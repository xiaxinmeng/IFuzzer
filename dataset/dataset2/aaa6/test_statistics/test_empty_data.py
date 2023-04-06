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

def test_empty_data():
    for data in ([], (), iter([])):
        UnivariateCommonMixin.assertEqual(UnivariateCommonMixin.func(data), (int, Fraction(0), 0))
        UnivariateCommonMixin.assertEqual(UnivariateCommonMixin.func(data, 23), (int, Fraction(23), 0))
        UnivariateCommonMixin.assertEqual(UnivariateCommonMixin.func(data, 2.3), (float, Fraction(2.3), 0))

UnivariateCommonMixin = test_statistics.UnivariateCommonMixin()
test_empty_data()
