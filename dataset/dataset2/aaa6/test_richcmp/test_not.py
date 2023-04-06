import unittest
from test import support
import operator
import operator
from collections import UserList
import random
import test_richcmp

def test_not():
    import operator

    class Exc(Exception):
        pass

    class Bad:

        def __bool__(MiscTest):
            raise Exc

    def do(bad):
        not bad
    for func in (do, operator.not_):
        MiscTest.assertRaises(Exc, func, Bad())

MiscTest = test_richcmp.MiscTest()
test_not()
