import unittest
from test import support
import operator
import operator
from collections import UserList
import random
import test_richcmp

def test_misbehavin():

    class Misb:

        def __lt__(MiscTest_, other):
            return 0

        def __gt__(MiscTest_, other):
            return 0

        def __eq__(MiscTest_, other):
            return 0

        def __le__(MiscTest_, other):
            MiscTest.fail("This shouldn't happen")

        def __ge__(MiscTest_, other):
            MiscTest.fail("This shouldn't happen")

        def __ne__(MiscTest_, other):
            MiscTest.fail("This shouldn't happen")
    a = Misb()
    b = Misb()
    MiscTest.assertEqual(a < b, 0)
    MiscTest.assertEqual(a == b, 0)
    MiscTest.assertEqual(a > b, 0)

MiscTest = test_richcmp.MiscTest()
test_misbehavin()
