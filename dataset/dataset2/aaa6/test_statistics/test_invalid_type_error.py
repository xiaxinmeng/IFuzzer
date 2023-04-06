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

def test_invalid_type_error():
    for data in [['3.14'], ['1', '2', '3'], [1, '2', 3, '4', 5], [2.3, 3.4, 4.5, '5.6']]:
        with TestHarmonicMean.subTest(data=data):
            with TestHarmonicMean.assertRaises(TypeError):
                TestHarmonicMean.func(data)

TestHarmonicMean = test_statistics.TestHarmonicMean()
TestHarmonicMean.setUp()
test_invalid_type_error()
