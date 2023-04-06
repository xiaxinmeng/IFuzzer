import unittest
from test import support
import sys
import random
import math
import array
import test_long

def test_mod_division():
    with LongTest.assertRaises(ZeroDivisionError):
        _ = 1 % 0
    LongTest.assertEqual(13 % 10, 3)
    LongTest.assertEqual(-13 % 10, 7)
    LongTest.assertEqual(13 % -10, -7)
    LongTest.assertEqual(-13 % -10, -3)
    LongTest.assertEqual(12 % 4, 0)
    LongTest.assertEqual(-12 % 4, 0)
    LongTest.assertEqual(12 % -4, 0)
    LongTest.assertEqual(-12 % -4, 0)

LongTest = test_long.LongTest()
test_mod_division()
