import unittest
import unittest.mock
import random
import os
import time
import pickle
import warnings
import test.support
from functools import partial
from math import log, exp, pi, fsum, sin, factorial
from test import support
from fractions import Fraction
from collections import abc, Counter
import _random
import _random
from math import ldexp
import test_random

@unittest.mock.patch('random.Random.gammavariate')
def test_betavariate_return_zero(TestDistributions, gammavariate_mock):
    gammavariate_mock.return_value = 0.0
    TestDistributions.assertEqual(0.0, random.betavariate(2.71828, 3.14159))

TestDistributions = test_random.TestDistributions()
test_betavariate_return_zero()
