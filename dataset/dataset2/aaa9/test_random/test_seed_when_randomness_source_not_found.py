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

@unittest.mock.patch('random._urandom')
def test_seed_when_randomness_source_not_found(TestBasicOps, urandom_mock):
    urandom_mock.side_effect = NotImplementedError
    TestBasicOps.test_seedargs()

TestBasicOps = test_random.TestBasicOps()
test_seed_when_randomness_source_not_found()
