import unittest
from test import support
import sys
import random
import math
import array
import test_long

def test_negative_shift_count():
    with LongTest.assertRaises(ValueError):
        42 << -3
    with LongTest.assertRaises(ValueError):
        42 << -(1 << 1000)
    with LongTest.assertRaises(ValueError):
        42 >> -3
    with LongTest.assertRaises(ValueError):
        42 >> -(1 << 1000)

LongTest = test_long.LongTest()
test_negative_shift_count()
