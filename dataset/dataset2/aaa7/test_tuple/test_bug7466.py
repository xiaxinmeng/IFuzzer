from test import support, seq_tests
import unittest
import gc
import pickle
from itertools import product
from collections import Counter
import sys
import test_tuple

@support.cpython_only
def test_bug7466():
    TupleTest._not_tracked(tuple((gc.collect() for i in range(101))))

TupleTest = test_tuple.TupleTest()
test_bug7466()
