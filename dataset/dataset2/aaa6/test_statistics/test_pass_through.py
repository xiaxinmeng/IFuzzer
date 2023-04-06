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

def test_pass_through():
    values = [1, 2.0, Fraction(3), Decimal(4)]
    new = list(statistics._fail_neg(values))
    FailNegTest.assertEqual(values, new)

FailNegTest = test_statistics.FailNegTest()
test_pass_through()
