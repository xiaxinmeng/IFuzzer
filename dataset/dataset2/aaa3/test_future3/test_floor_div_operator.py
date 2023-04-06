from __future__ import nested_scopes
from __future__ import division
import unittest
import test_future3

def test_floor_div_operator():
    TestFuture.assertEqual(7 // 2, 3)

TestFuture = test_future3.TestFuture()
test_floor_div_operator()
