from test import support, seq_tests
import unittest
import gc
import pickle
from itertools import product
from collections import Counter
import sys
import test_tuple

def test_constructors():
    super().test_constructors()
    TupleTest.assertEqual(tuple(), ())
    t0_3 = (0, 1, 2, 3)
    t0_3_bis = tuple(t0_3)
    TupleTest.assertTrue(t0_3 is t0_3_bis)
    TupleTest.assertEqual(tuple([]), ())
    TupleTest.assertEqual(tuple([0, 1, 2, 3]), (0, 1, 2, 3))
    TupleTest.assertEqual(tuple(''), ())
    TupleTest.assertEqual(tuple('spam'), ('s', 'p', 'a', 'm'))
    TupleTest.assertEqual(tuple((x for x in range(10) if x % 2)), (1, 3, 5, 7, 9))

TupleTest = test_tuple.TupleTest()
TupleTest.setUp()
test_constructors()
