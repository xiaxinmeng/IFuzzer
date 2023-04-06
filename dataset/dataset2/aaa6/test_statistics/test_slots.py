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

def test_slots():
    nd = TestNormalDist.module.NormalDist(300, 23)
    with TestNormalDist.assertRaises(TypeError):
        vars(nd)
    TestNormalDist.assertEqual(tuple(nd.__slots__), ('_mu', '_sigma'))

TestNormalDist = test_statistics.TestNormalDist()
test_slots()
