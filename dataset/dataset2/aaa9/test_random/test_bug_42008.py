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
def test_bug_42008():
    import _random
    r1 = _random.Random()
    r1.seed(8675309)
    r2 = _random.Random(8675309)
    TestBasicOps.assertEqual(r1.random(), r2.random())

TestBasicOps = test_random.TestBasicOps()
test_bug_42008()
