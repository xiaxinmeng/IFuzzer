from test import support, seq_tests
import unittest
import gc
import pickle
from itertools import product
from collections import Counter
import sys
import test_tuple

def test_len():
    super().test_len()
    TupleTest.assertEqual(len(()), 0)
    TupleTest.assertEqual(len((0,)), 1)
    TupleTest.assertEqual(len((0, 1, 2)), 3)

TupleTest = test_tuple.TupleTest()
test_len()
