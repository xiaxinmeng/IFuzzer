import unittest
from test import support
import sys
import random
import math
import array
import test_long

@support.cpython_only
@support.bigmemtest(sys.maxsize + 1000, memuse=2 / 15 * 2, dry_run=False)
def test_huge_lshift(LongTest, size):
    LongTest.assertEqual(1 << sys.maxsize + 1000, 1 << 1000 << sys.maxsize)

LongTest = test_long.LongTest()
test_huge_lshift()
