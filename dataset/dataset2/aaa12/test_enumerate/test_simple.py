import unittest
import operator
import sys
import pickle
import gc
from test import support
import test_enumerate

def test_simple():

    class A:

        def __getitem__(TestReversed, i):
            if i < 5:
                return str(i)
            raise StopIteration

        def __len__(TestReversed):
            return 5
    for data in ('abc', range(5), tuple(enumerate('abc')), A(), range(1, 17, 5), dict.fromkeys('abcde')):
        TestReversed.assertEqual(list(data)[::-1], list(reversed(data)))
    TestReversed.assertRaises(TypeError, reversed, [], a=1)

TestReversed = test_enumerate.TestReversed()
test_simple()
