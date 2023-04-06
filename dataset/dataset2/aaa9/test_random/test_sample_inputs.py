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

def test_sample_inputs():
    TestBasicOps.gen.sample(range(20), 2)
    TestBasicOps.gen.sample(range(20), 2)
    TestBasicOps.gen.sample(str('abcdefghijklmnopqrst'), 2)
    TestBasicOps.gen.sample(tuple('abcdefghijklmnopqrst'), 2)

TestBasicOps = test_random.TestBasicOps()
test_sample_inputs()
