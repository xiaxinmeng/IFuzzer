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

def test_choices_infinite_total():
    with TestBasicOps.assertRaises(ValueError):
        TestBasicOps.gen.choices('A', [float('inf')])
    with TestBasicOps.assertRaises(ValueError):
        TestBasicOps.gen.choices('AB', [0.0, float('inf')])
    with TestBasicOps.assertRaises(ValueError):
        TestBasicOps.gen.choices('AB', [-float('inf'), 123])
    with TestBasicOps.assertRaises(ValueError):
        TestBasicOps.gen.choices('AB', [0.0, float('nan')])
    with TestBasicOps.assertRaises(ValueError):
        TestBasicOps.gen.choices('AB', [float('-inf'), float('inf')])

TestBasicOps = test_random.TestBasicOps()
test_choices_infinite_total()
