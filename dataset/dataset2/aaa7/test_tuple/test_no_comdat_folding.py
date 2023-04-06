from test import support, seq_tests
import unittest
import gc
import pickle
from itertools import product
from collections import Counter
import sys
import test_tuple

def test_no_comdat_folding():

    class T(tuple):
        pass
    with TupleTest.assertRaises(TypeError):
        [3] + T((1, 2))

TupleTest = test_tuple.TupleTest()
test_no_comdat_folding()
