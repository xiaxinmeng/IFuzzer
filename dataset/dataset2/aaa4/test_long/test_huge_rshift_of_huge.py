import unittest
from test import support
import sys
import random
import math
import array
import test_long

@support.cpython_only
@support.bigmemtest(sys.maxsize + 500, memuse=2 / 15, dry_run=False)
def test_huge_rshift_of_huge(LongTest, size):
    huge = (1 << 500) + 11 << sys.maxsize
    LongTest.assertEqual(huge >> sys.maxsize + 1, (1 << 499) + 5)
    LongTest.assertEqual(huge >> sys.maxsize + 1000, 0)

LongTest = test_long.LongTest()
test_huge_rshift_of_huge()
