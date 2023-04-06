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

def test_53_bits_per_float():
    span = 2 ** 53
    cum = 0
    for i in range(100):
        cum |= int(SystemRandom_TestBasicOps.gen.random() * span)
    SystemRandom_TestBasicOps.assertEqual(cum, span - 1)

SystemRandom_TestBasicOps = test_random.SystemRandom_TestBasicOps()
test_53_bits_per_float()
