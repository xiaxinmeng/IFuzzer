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

def test_hashability():
    ND = TestNormalDist.module.NormalDist
    s = {ND(100, 15), ND(100.0, 15.0), ND(100, 10), ND(95, 15), ND(100, 15)}
    TestNormalDist.assertEqual(len(s), 3)

TestNormalDist = test_statistics.TestNormalDist()
test_hashability()
