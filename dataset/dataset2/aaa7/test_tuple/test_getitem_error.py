from test import support, seq_tests
import unittest
import gc
import pickle
from itertools import product
from collections import Counter
import sys
import test_tuple

def test_getitem_error():
    t = ()
    msg = 'tuple indices must be integers or slices'
    with TupleTest.assertRaisesRegex(TypeError, msg):
        t['a']

TupleTest = test_tuple.TupleTest()
test_getitem_error()
