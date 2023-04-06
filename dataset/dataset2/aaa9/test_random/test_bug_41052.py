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

@test.support.cpython_only
def test_bug_41052():
    import _random
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        r = _random.Random()
        TestBasicOps.assertRaises(TypeError, pickle.dumps, r, proto)

TestBasicOps = test_random.TestBasicOps()
test_bug_41052()
