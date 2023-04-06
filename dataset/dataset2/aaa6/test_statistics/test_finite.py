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

def test_finite():
    for x in (5, Fraction(1, 3), 2.5, Decimal('5.5')):
        IsFiniteTest.assertTrue(statistics._isfinite(x))

IsFiniteTest = test_statistics.IsFiniteTest()
test_finite()
