import unittest
from test import support
from test.support import os_helper
import os
import operator
import marshal
import pickle
import pickle
import test_bool

def test_operator():
    import operator
    BoolTest.assertIs(operator.truth(0), False)
    BoolTest.assertIs(operator.truth(1), True)
    BoolTest.assertIs(operator.not_(1), False)
    BoolTest.assertIs(operator.not_(0), True)
    BoolTest.assertIs(operator.contains([], 1), False)
    BoolTest.assertIs(operator.contains([1], 1), True)
    BoolTest.assertIs(operator.lt(0, 0), False)
    BoolTest.assertIs(operator.lt(0, 1), True)
    BoolTest.assertIs(operator.is_(True, True), True)
    BoolTest.assertIs(operator.is_(True, False), False)
    BoolTest.assertIs(operator.is_not(True, True), False)
    BoolTest.assertIs(operator.is_not(True, False), True)

BoolTest = test_bool.BoolTest()
test_operator()
