import unittest
from test import support
from test.support import os_helper
import os
import operator
import marshal
import pickle
import pickle
import test_bool

def test_issubclass():
    BoolTest.assertIs(issubclass(bool, int), True)
    BoolTest.assertIs(issubclass(int, bool), False)

BoolTest = test_bool.BoolTest()
test_issubclass()
