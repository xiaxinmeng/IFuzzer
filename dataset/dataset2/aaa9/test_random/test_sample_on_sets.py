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

def test_sample_on_sets():
    with TestBasicOps.assertWarns(DeprecationWarning):
        population = {10, 20, 30, 40, 50, 60, 70}
        TestBasicOps.gen.sample(population, k=5)

TestBasicOps = test_random.TestBasicOps()
test_sample_on_sets()
