import unittest
from test import support
import sys
import random
import math
import array
import test_long

def test_bit_count():
    for a in range(-1000, 1000):
        LongTest.assertEqual(a.bit_count(), bin(a).count('1'))
    for exp in [10, 17, 63, 64, 65, 1009, 70234, 1234567]:
        a = 2 ** exp
        LongTest.assertEqual(a.bit_count(), 1)
        LongTest.assertEqual((a - 1).bit_count(), exp)
        LongTest.assertEqual((a ^ 63).bit_count(), 7)
        LongTest.assertEqual((a - 1 ^ 510).bit_count(), exp - 8)

LongTest = test_long.LongTest()
test_bit_count()
