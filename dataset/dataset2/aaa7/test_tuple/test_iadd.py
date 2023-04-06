from test import support, seq_tests
import unittest
import gc
import pickle
from itertools import product
from collections import Counter
import sys
import test_tuple

def test_iadd():
    super().test_iadd()
    u = (0, 1)
    u2 = u
    u += (2, 3)
    TupleTest.assertTrue(u is not u2)

TupleTest = test_tuple.TupleTest()
test_iadd()
