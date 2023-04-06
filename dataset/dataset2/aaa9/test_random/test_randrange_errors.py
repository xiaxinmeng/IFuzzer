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

def test_randrange_errors():
    raises = partial(SystemRandom_TestBasicOps.assertRaises, ValueError, SystemRandom_TestBasicOps.gen.randrange)
    raises(3, 3)
    raises(-721)
    raises(0, 100, -12)
    raises(3.14159)
    raises(0, 2.71828)
    raises(0, 42, 0)
    raises(0, 42, 3.14159)

SystemRandom_TestBasicOps = test_random.SystemRandom_TestBasicOps()
test_randrange_errors()
