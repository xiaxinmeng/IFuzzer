from test import support, seq_tests
import unittest
import gc
import pickle
from itertools import product
from collections import Counter
import sys
import test_tuple

def test_keyword_args():
    with TupleTest.assertRaisesRegex(TypeError, 'keyword argument'):
        tuple(sequence=())

TupleTest = test_tuple.TupleTest()
test_keyword_args()
