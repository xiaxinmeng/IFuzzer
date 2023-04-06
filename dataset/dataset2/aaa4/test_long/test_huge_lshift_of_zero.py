import unittest
from test import support
import sys
import random
import math
import array
import test_long

@support.cpython_only
def test_huge_lshift_of_zero():
    LongTest.assertEqual(0 << sys.maxsize, 0)
    LongTest.assertEqual(0 << sys.maxsize + 1, 0)

LongTest = test_long.LongTest()
test_huge_lshift_of_zero()
