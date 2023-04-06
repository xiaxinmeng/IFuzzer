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

@unittest.mock.patch('random.Random.random')
def test_gammavariate_alpha_greater_one(TestDistributions, random_mock):
    random_mock.side_effect = [1e-08, 0.5, 0.3]
    returned_value = random.gammavariate(1.1, 2.3)
    TestDistributions.assertAlmostEqual(returned_value, 2.53)

TestDistributions = test_random.TestDistributions()
test_gammavariate_alpha_greater_one()
