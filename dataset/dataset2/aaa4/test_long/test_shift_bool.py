import unittest
from test import support
import sys
import random
import math
import array
import test_long

def test_shift_bool():
    for value in (True, False):
        for shift in (0, 2):
            LongTest.assertEqual(type(value << shift), int)
            LongTest.assertEqual(type(value >> shift), int)

LongTest = test_long.LongTest()
test_shift_bool()
