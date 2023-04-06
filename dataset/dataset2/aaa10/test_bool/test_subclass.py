import unittest
from test import support
from test.support import os_helper
import os
import operator
import marshal
import pickle
import pickle
import test_bool

def test_subclass():
    try:

        class C(bool):
            pass
    except TypeError:
        pass
    else:
        BoolTest.fail('bool should not be subclassable')
    BoolTest.assertRaises(TypeError, int.__new__, bool, 0)

BoolTest = test_bool.BoolTest()
test_subclass()
