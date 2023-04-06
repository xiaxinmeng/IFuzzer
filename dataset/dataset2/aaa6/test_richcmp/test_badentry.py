import unittest
from test import support
import operator
import operator
from collections import UserList
import random
import test_richcmp

def test_badentry():

    class Exc(Exception):
        pass

    class Bad:

        def __eq__(ListTest, other):
            raise Exc
    x = [Bad()]
    y = [Bad()]
    for op in test_richcmp.opmap['eq']:
        ListTest.assertRaises(Exc, op, x, y)

ListTest = test_richcmp.ListTest()
test_badentry()
