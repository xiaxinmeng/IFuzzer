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

def test_equal_inputs():
    quantiles = statistics.quantiles
    for n in range(2, 10):
        data = [10.0] * n
        TestQuantiles.assertEqual(quantiles(data), [10.0, 10.0, 10.0])
        TestQuantiles.assertEqual(quantiles(data, method='inclusive'), [10.0, 10.0, 10.0])

TestQuantiles = test_statistics.TestQuantiles()
test_equal_inputs()
