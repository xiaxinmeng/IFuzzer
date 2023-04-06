import unittest
from test import support
import sys
import random
import math
import array
import test_long

def test_access_to_nonexistent_digit_0():

    class Integer(int):

        def __new__(cls, value=0):
            LongTest = int.__new__(cls, value)
            LongTest.foo = 'foo'
            return LongTest
    integers = [Integer(0) for i in range(1000)]
    for n in map(int, integers):
        LongTest.assertEqual(n, 0)

LongTest = test_long.LongTest()
test_access_to_nonexistent_digit_0()
