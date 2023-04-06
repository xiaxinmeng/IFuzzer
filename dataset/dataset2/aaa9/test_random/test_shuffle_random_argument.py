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

def test_shuffle_random_argument():
    shuffle = TestBasicOps.gen.shuffle
    mock_random = unittest.mock.Mock(return_value=0.5)
    seq = bytearray(b'abcdefghijk')
    with TestBasicOps.assertWarns(DeprecationWarning):
        shuffle(seq, mock_random)
    mock_random.assert_called_with()

TestBasicOps = test_random.TestBasicOps()
test_shuffle_random_argument()
