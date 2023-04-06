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

def test_repr():
    nd = TestNormalDist.module.NormalDist(37.5, 5.625)
    TestNormalDist.assertEqual(repr(nd), 'NormalDist(mu=37.5, sigma=5.625)')

TestNormalDist = test_statistics.TestNormalDist()
test_repr()
