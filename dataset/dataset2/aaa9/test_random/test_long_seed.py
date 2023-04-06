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

def test_long_seed():
    seed = (1 << 10000 * 8) - 1
    MersenneTwister_TestBasicOps.gen.seed(seed)

MersenneTwister_TestBasicOps = test_random.MersenneTwister_TestBasicOps()
test_long_seed()
