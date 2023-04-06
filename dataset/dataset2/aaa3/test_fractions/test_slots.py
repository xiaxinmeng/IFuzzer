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

def test_slots():
    r = test_fractions.F(13, 7)
    FractionTest.assertRaises(AttributeError, setattr, r, 'a', 10)

FractionTest = test_fractions.FractionTest()
test_slots()
