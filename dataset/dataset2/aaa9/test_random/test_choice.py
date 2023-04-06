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

def test_choice():
    choice = TestBasicOps.gen.choice
    with TestBasicOps.assertRaises(IndexError):
        choice([])
    TestBasicOps.assertEqual(choice([50]), 50)
    TestBasicOps.assertIn(choice([25, 75]), [25, 75])

TestBasicOps = test_random.TestBasicOps()
test_choice()
