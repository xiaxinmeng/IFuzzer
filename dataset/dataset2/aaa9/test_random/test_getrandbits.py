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

def test_getrandbits():
    super().test_getrandbits()
    TestBasicOps.gen.seed(1234567)
    TestBasicOps.assertEqual(TestBasicOps.gen.getrandbits(100), 97904845777343510404718956115)

TestBasicOps = test_random.TestBasicOps()
test_getrandbits()
