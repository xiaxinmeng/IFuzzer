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

def test_strong_reference_implementation():
    from math import ldexp
    expected = [4128882400830239, 7751398889519013, 8363034243334166, 3236528186029503, 737000512037440, 1290932195808883, 759287295919497, 4847212089661076, 803577505899006, 7069408070677702]
    MersenneTwister_TestBasicOps.gen.seed(61731 + (24903 << 32) + (614 << 64) + (42143 << 96))
    actual = MersenneTwister_TestBasicOps.randomlist(2000)[-10:]
    for (a, e) in zip(actual, expected):
        MersenneTwister_TestBasicOps.assertEqual(int(ldexp(a, 53)), e)

MersenneTwister_TestBasicOps = test_random.MersenneTwister_TestBasicOps()
test_strong_reference_implementation()
