import unittest
from test import support
import operator
import operator
from collections import UserList
import random
import test_richcmp

def test_values():
    NumberTest.checkvalue('lt', 0, 0, False)
    NumberTest.checkvalue('le', 0, 0, True)
    NumberTest.checkvalue('eq', 0, 0, True)
    NumberTest.checkvalue('ne', 0, 0, False)
    NumberTest.checkvalue('gt', 0, 0, False)
    NumberTest.checkvalue('ge', 0, 0, True)
    NumberTest.checkvalue('lt', 0, 1, True)
    NumberTest.checkvalue('le', 0, 1, True)
    NumberTest.checkvalue('eq', 0, 1, False)
    NumberTest.checkvalue('ne', 0, 1, True)
    NumberTest.checkvalue('gt', 0, 1, False)
    NumberTest.checkvalue('ge', 0, 1, False)
    NumberTest.checkvalue('lt', 1, 0, False)
    NumberTest.checkvalue('le', 1, 0, False)
    NumberTest.checkvalue('eq', 1, 0, False)
    NumberTest.checkvalue('ne', 1, 0, True)
    NumberTest.checkvalue('gt', 1, 0, True)
    NumberTest.checkvalue('ge', 1, 0, True)

NumberTest = test_richcmp.NumberTest()
test_values()
