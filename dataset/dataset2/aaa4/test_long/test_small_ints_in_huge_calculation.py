import unittest
from test import support
import sys
import random
import math
import array
import test_long

@support.cpython_only
def test_small_ints_in_huge_calculation():
    a = 2 ** 100
    b = -a + 1
    c = a + 1
    LongTest.assertIs(a + b, 1)
    LongTest.assertIs(c - a, 1)

LongTest = test_long.LongTest()
test_small_ints_in_huge_calculation()
