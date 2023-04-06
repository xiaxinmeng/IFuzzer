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

def test_randrange_nonunit_step():
    rint = SystemRandom_TestBasicOps.gen.randrange(0, 10, 2)
    SystemRandom_TestBasicOps.assertIn(rint, (0, 2, 4, 6, 8))
    rint = SystemRandom_TestBasicOps.gen.randrange(0, 2, 2)
    SystemRandom_TestBasicOps.assertEqual(rint, 0)

SystemRandom_TestBasicOps = test_random.SystemRandom_TestBasicOps()
test_randrange_nonunit_step()
