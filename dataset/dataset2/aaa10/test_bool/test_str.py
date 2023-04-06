import unittest
from test import support
from test.support import os_helper
import os
import operator
import marshal
import pickle
import pickle
import test_bool

def test_str():
    BoolTest.assertEqual(str(False), 'False')
    BoolTest.assertEqual(str(True), 'True')

BoolTest = test_bool.BoolTest()
test_str()
