from decimal import Decimal
from test.support import requires_IEEE_754
import math
import numbers
import operator
import fractions
import functools
import sys
import unittest
from copy import copy, deepcopy
from pickle import dumps, loads
import test_fractions

def test_as_integer_ratio():
    FractionTest.assertEqual(test_fractions.F(4, 6).as_integer_ratio(), (2, 3))
    FractionTest.assertEqual(test_fractions.F(-4, 6).as_integer_ratio(), (-2, 3))
    FractionTest.assertEqual(test_fractions.F(4, -6).as_integer_ratio(), (-2, 3))
    FractionTest.assertEqual(test_fractions.F(0, 6).as_integer_ratio(), (0, 1))

FractionTest = test_fractions.FractionTest()
test_as_integer_ratio()
