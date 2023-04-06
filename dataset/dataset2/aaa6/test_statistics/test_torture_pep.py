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

def test_torture_pep():
    TestMean.assertEqual(TestMean.func([1e+100, 1, 3, -1e+100]), 1)

TestMean = test_statistics.TestMean()
TestMean.setUp()
test_torture_pep()
