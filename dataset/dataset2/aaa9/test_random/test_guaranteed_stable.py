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

def test_guaranteed_stable():
    MersenneTwister_TestBasicOps.gen.seed(3456147, version=1)
    MersenneTwister_TestBasicOps.assertEqual([MersenneTwister_TestBasicOps.gen.random().hex() for i in range(4)], ['0x1.ac362300d90d2p-1', '0x1.9d16f74365005p-1', '0x1.1ebb4352e4c4dp-1', '0x1.1a7422abf9c11p-1'])
    MersenneTwister_TestBasicOps.gen.seed('the quick brown fox', version=2)
    MersenneTwister_TestBasicOps.assertEqual([MersenneTwister_TestBasicOps.gen.random().hex() for i in range(4)], ['0x1.1239ddfb11b7cp-3', '0x1.b3cbb5c51b120p-4', '0x1.8c4f55116b60fp-1', '0x1.63eb525174a27p-1'])

MersenneTwister_TestBasicOps = test_random.MersenneTwister_TestBasicOps()
test_guaranteed_stable()
