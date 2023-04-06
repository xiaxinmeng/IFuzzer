from test import support, seq_tests
import unittest
import gc
import pickle
from itertools import product
from collections import Counter
import sys
import test_tuple

def test_lexicographic_ordering():
    a = TupleTest.type2test([1, 2])
    b = TupleTest.type2test([1, 2, 0])
    c = TupleTest.type2test([1, 3])
    TupleTest.assertLess(a, b)
    TupleTest.assertLess(b, c)

TupleTest = test_tuple.TupleTest()
test_lexicographic_ordering()
