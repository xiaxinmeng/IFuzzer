from test import support, seq_tests
import unittest
import gc
import pickle
from itertools import product
from collections import Counter
import sys
import test_tuple

def test_tupleresizebug():

    def f():
        for i in range(1000):
            yield i
    TupleTest.assertEqual(list(tuple(f())), list(range(1000)))

TupleTest = test_tuple.TupleTest()
test_tupleresizebug()
