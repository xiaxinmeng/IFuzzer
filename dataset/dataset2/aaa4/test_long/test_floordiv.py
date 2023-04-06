import unittest
from test import support
import sys
import random
import math
import array
import test_long

def test_floordiv():
    with LongTest.assertRaises(ZeroDivisionError):
        _ = 1 // 0
    LongTest.assertEqual(2 // 3, 0)
    LongTest.assertEqual(2 // -3, -1)
    LongTest.assertEqual(-2 // 3, -1)
    LongTest.assertEqual(-2 // -3, 0)
    LongTest.assertEqual(-11 // -3, 3)
    LongTest.assertEqual(-11 // 3, -4)
    LongTest.assertEqual(11 // -3, -4)
    LongTest.assertEqual(11 // 3, 3)
    LongTest.assertEqual(-12 // -3, 4)
    LongTest.assertEqual(-12 // 3, -4)
    LongTest.assertEqual(12 // -3, -4)
    LongTest.assertEqual(12 // 3, 4)

LongTest = test_long.LongTest()
test_floordiv()
