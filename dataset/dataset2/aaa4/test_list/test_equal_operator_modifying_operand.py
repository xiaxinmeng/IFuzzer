import sys
from test import list_tests
from test.support import cpython_only
import pickle
import unittest
import test_list

def test_equal_operator_modifying_operand():

    class X:

        def __eq__(ListTest, other):
            list2.clear()
            return NotImplemented

    class Y:

        def __eq__(ListTest, other):
            list1.clear()
            return NotImplemented

    class Z:

        def __eq__(ListTest, other):
            list3.clear()
            return NotImplemented
    list1 = [X()]
    list2 = [Y()]
    ListTest.assertTrue(list1 == list2)
    list3 = [Z()]
    list4 = [1]
    ListTest.assertFalse(list3 == list4)

ListTest = test_list.ListTest()
test_equal_operator_modifying_operand()
