import unittest
from test import support
from test.support import os_helper
import os
import operator
import marshal
import pickle
import pickle
import test_bool

def test_callable():
    BoolTest.assertIs(callable(len), True)
    BoolTest.assertIs(callable(1), False)

BoolTest = test_bool.BoolTest()
test_callable()
