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

def test_choices_subnormal():
    choices = TestBasicOps.gen.choices
    choices(population=[1, 2], weights=[1e-323, 1e-323], k=5000)

TestBasicOps = test_random.TestBasicOps()
test_choices_subnormal()
