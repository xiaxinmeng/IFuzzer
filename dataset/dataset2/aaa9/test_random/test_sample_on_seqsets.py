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

def test_sample_on_seqsets():

    class SeqSet(abc.Sequence, abc.Set):

        def __init__(TestBasicOps, items):
            TestBasicOps._items = items

        def __len__(TestBasicOps):
            return len(TestBasicOps._items)

        def __getitem__(TestBasicOps, index):
            return TestBasicOps._items[index]
    population = SeqSet([2, 4, 1, 3])
    with warnings.catch_warnings():
        warnings.simplefilter('error', DeprecationWarning)
        TestBasicOps.gen.sample(population, k=2)

TestBasicOps = test_random.TestBasicOps()
test_sample_on_seqsets()
