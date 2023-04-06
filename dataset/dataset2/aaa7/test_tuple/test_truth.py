from test import support, seq_tests
import unittest
import gc
import pickle
from itertools import product
from collections import Counter
import sys
import test_tuple

def test_truth():
    super().test_truth()
    TupleTest.assertTrue(not ())
    TupleTest.assertTrue((42,))

TupleTest = test_tuple.TupleTest()
test_truth()
