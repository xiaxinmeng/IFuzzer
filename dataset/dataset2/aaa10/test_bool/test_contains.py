import unittest
from test import support
from test.support import os_helper
import os
import operator
import marshal
import pickle
import pickle
import test_bool

def test_contains():
    BoolTest.assertIs(1 in {}, False)
    BoolTest.assertIs(1 in {1: 1}, True)

BoolTest = test_bool.BoolTest()
test_contains()
