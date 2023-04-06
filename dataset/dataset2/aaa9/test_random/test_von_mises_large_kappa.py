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

def test_von_mises_large_kappa():
    random.vonmisesvariate(0, 1000000000000000.0)
    random.vonmisesvariate(0, 1e+100)

TestDistributions = test_random.TestDistributions()
test_von_mises_large_kappa()
