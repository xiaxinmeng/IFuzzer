import unittest
import operator
import sys
import pickle
import gc
from test import support
import test_enumerate

def test_pickle():
    for data in ('abc', range(5), tuple(enumerate('abc')), range(1, 17, 5)):
        EnumerateTestCase.check_pickle(reversed(data), list(data)[::-1])

EnumerateTestCase = test_enumerate.EnumerateTestCase()
test_pickle()
