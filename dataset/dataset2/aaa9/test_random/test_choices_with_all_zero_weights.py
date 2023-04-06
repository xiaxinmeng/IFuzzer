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

def test_choices_with_all_zero_weights():
    with TestBasicOps.assertRaises(ValueError):
        TestBasicOps.gen.choices('AB', [0.0, 0.0])

TestBasicOps = test_random.TestBasicOps()
test_choices_with_all_zero_weights()
