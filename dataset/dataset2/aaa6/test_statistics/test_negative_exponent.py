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

def test_negative_exponent():
    t = statistics._exact_ratio(Decimal('0.1234'))
    DecimalToRatioTest.assertEqual(t, (617, 5000))

DecimalToRatioTest = test_statistics.DecimalToRatioTest()
test_negative_exponent()
