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

def test_randrange_uses_getrandbits():
    MersenneTwister_TestBasicOps.gen.seed(1234567)
    MersenneTwister_TestBasicOps.assertEqual(MersenneTwister_TestBasicOps.gen.randrange(2 ** 99), 97904845777343510404718956115)

MersenneTwister_TestBasicOps = test_random.MersenneTwister_TestBasicOps()
test_randrange_uses_getrandbits()
