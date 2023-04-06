from test import support, seq_tests
import unittest
import gc
import pickle
from itertools import product
from collections import Counter
import sys
import test_tuple

@support.cpython_only
def test_track_dynamic():
    TupleTest.check_track_dynamic(tuple, False)

TupleTest = test_tuple.TupleTest()
test_track_dynamic()
