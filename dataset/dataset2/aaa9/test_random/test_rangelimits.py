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

def test_rangelimits():
    for (start, stop) in [(-2, 0), (-2 ** 60 - 2, -2 ** 60), (2 ** 60, 2 ** 60 + 2)]:
        SystemRandom_TestBasicOps.assertEqual(set(range(start, stop)), set([SystemRandom_TestBasicOps.gen.randrange(start, stop) for i in range(100)]))

SystemRandom_TestBasicOps = test_random.SystemRandom_TestBasicOps()
test_rangelimits()
