import unittest
import operator
import sys
import pickle
import gc
from test import support
import test_enumerate

def test_gc():

    class Seq:

        def __len__(TestReversed):
            return 10

        def __getitem__(TestReversed, index):
            return index
    s = Seq()
    r = reversed(s)
    s.r = r

TestReversed = test_enumerate.TestReversed()
test_gc()
