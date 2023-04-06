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

def test_random_subclass_with_kwargs():

    class Subclass(random.Random):

        def __init__(TestRandomSubclassing, newarg=None):
            random.Random.__init__(TestRandomSubclassing)
    Subclass(newarg=1)

TestRandomSubclassing = test_random.TestRandomSubclassing()
test_random_subclass_with_kwargs()
