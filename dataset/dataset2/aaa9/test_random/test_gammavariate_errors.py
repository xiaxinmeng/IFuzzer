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

def test_gammavariate_errors():
    TestDistributions.assertRaises(ValueError, random.gammavariate, -1, 3)
    TestDistributions.assertRaises(ValueError, random.gammavariate, 0, 2)
    TestDistributions.assertRaises(ValueError, random.gammavariate, 2, 0)
    TestDistributions.assertRaises(ValueError, random.gammavariate, 1, -3)

TestDistributions = test_random.TestDistributions()
test_gammavariate_errors()
