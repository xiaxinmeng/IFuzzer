from __future__ import nested_scopes
from __future__ import division
import unittest
import test_future3

def nester():
    x = 3
    def inner():
        return x
    return inner()

def test_nested_scopes():
    TestFuture.assertEqual(nester(), 3)

TestFuture = test_future3.TestFuture()
test_nested_scopes()
