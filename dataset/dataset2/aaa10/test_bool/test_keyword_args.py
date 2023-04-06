import unittest
from test import support
from test.support import os_helper
import os
import operator
import marshal
import pickle
import pickle
import test_bool

def test_keyword_args():
    with BoolTest.assertRaisesRegex(TypeError, 'keyword argument'):
        bool(x=10)

BoolTest = test_bool.BoolTest()
test_keyword_args()
