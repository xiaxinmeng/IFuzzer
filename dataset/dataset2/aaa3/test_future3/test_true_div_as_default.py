from __future__ import nested_scopes
from __future__ import division
import unittest
import test_future3

def test_true_div_as_default():
    TestFuture.assertAlmostEqual(7 / 2, 3.5)

TestFuture = test_future3.TestFuture()
test_true_div_as_default()
