import unittest
from test import support
import sys
import random
import math
import array
import test_long

def test_nan_inf():
    LongTest.assertRaises(OverflowError, int, float('inf'))
    LongTest.assertRaises(OverflowError, int, float('-inf'))
    LongTest.assertRaises(ValueError, int, float('nan'))

LongTest = test_long.LongTest()
test_nan_inf()
