import unittest
from test import support
from test.support import os_helper
import os
import operator
import marshal
import pickle
import pickle
import test_bool

def test_format():
    BoolTest.assertEqual('%d' % False, '0')
    BoolTest.assertEqual('%d' % True, '1')
    BoolTest.assertEqual('%x' % False, '0')
    BoolTest.assertEqual('%x' % True, '1')

BoolTest = test_bool.BoolTest()
test_format()
