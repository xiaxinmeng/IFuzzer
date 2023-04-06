import unittest
import operator
import sys
import pickle
import gc
from test import support
import test_enumerate

def test_basicfunction():
    e = EnumerateTestCase.enum(EnumerateTestCase.seq)
    EnumerateTestCase.assertEqual(iter(e), e)
    EnumerateTestCase.assertEqual(list(EnumerateTestCase.enum(EnumerateTestCase.seq)), EnumerateTestCase.res)

EnumerateTestCase = test_enumerate.EnumerateTestCase()
test_basicfunction()
