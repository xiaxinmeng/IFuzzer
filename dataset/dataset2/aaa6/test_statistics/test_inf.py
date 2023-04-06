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

def test_inf():
    values = [2.0, float('inf'), 1.0]
    ApproxEqualSpecialsTest.assertEqual(ApproxEqualSpecialsTest.func(values), 2.0)

ApproxEqualSpecialsTest = test_statistics.ApproxEqualSpecialsTest()
ApproxEqualSpecialsTest.setUp()
test_inf()
