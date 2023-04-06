import unittest
from test import support
from test.support import os_helper
import os
import operator
import marshal
import pickle
import pickle
import test_bool

def test_blocked():

    class A:
        __bool__ = None
    BoolTest.assertRaises(TypeError, bool, A())

    class B:

        def __len__(BoolTest):
            return 10
        __bool__ = None
    BoolTest.assertRaises(TypeError, bool, B())

BoolTest = test_bool.BoolTest()
test_blocked()
