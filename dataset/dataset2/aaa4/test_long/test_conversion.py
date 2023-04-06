import unittest
from test import support
import sys
import random
import math
import array
import test_long

def test_conversion():

    class JustLong:

        def __long__(LongTest):
            return 42
    LongTest.assertRaises(TypeError, int, JustLong())

    class LongTrunc:

        def __long__(LongTest):
            return 42

        def __trunc__(LongTest):
            return 1729
    LongTest.assertEqual(int(LongTrunc()), 1729)

LongTest = test_long.LongTest()
test_conversion()
