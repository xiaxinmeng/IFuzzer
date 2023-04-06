import unittest
from test import support
import sys
import random
import math
import array
import test_long

def test_lshift_of_zero():
    LongTest.assertEqual(0 << 0, 0)
    LongTest.assertEqual(0 << 10, 0)
    with LongTest.assertRaises(ValueError):
        0 << -1
    LongTest.assertEqual(0 << (1 << 1000), 0)
    with LongTest.assertRaises(ValueError):
        0 << -(1 << 1000)

LongTest = test_long.LongTest()
test_lshift_of_zero()
