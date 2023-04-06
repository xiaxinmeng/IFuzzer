import unittest
from test import support
import sys
import random
import math
import array
import test_long

def test_huge_rshift():
    LongTest.assertEqual(42 >> (1 << 1000), 0)
    LongTest.assertEqual(-42 >> (1 << 1000), -1)

LongTest = test_long.LongTest()
test_huge_rshift()
