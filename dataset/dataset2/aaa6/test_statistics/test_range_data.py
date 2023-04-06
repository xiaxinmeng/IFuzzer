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

def test_range_data():
    data = range(20, 50, 3)
    UnivariateCommonMixin.assertEqual(UnivariateCommonMixin.func(data), 20)

UnivariateCommonMixin = test_statistics.UnivariateCommonMixin()
test_range_data()
