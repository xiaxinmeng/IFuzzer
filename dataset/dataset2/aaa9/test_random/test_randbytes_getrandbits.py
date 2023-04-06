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

def test_randbytes_getrandbits():
    seed = 2849427419
    gen2 = random.Random()
    MersenneTwister_TestBasicOps.gen.seed(seed)
    gen2.seed(seed)
    for n in range(9):
        MersenneTwister_TestBasicOps.assertEqual(MersenneTwister_TestBasicOps.gen.randbytes(n), gen2.getrandbits(n * 8).to_bytes(n, 'little'))

MersenneTwister_TestBasicOps = test_random.MersenneTwister_TestBasicOps()
test_randbytes_getrandbits()
