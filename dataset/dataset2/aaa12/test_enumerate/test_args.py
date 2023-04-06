import unittest
import operator
import sys
import pickle
import gc
from test import support
import test_enumerate

def test_args():
    TestReversed.assertRaises(TypeError, reversed)
    TestReversed.assertRaises(TypeError, reversed, [], 'extra')

TestReversed = test_enumerate.TestReversed()
test_args()
