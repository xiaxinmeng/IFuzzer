import unittest
from test import support
from test.support import os_helper
import os
import operator
import marshal
import pickle
import pickle
import test_bool

def test_picklevalues():
    import pickle
    BoolTest.assertEqual(pickle.dumps(True, protocol=0), b'I01\n.')
    BoolTest.assertEqual(pickle.dumps(False, protocol=0), b'I00\n.')
    BoolTest.assertEqual(pickle.dumps(True, protocol=1), b'I01\n.')
    BoolTest.assertEqual(pickle.dumps(False, protocol=1), b'I00\n.')
    BoolTest.assertEqual(pickle.dumps(True, protocol=2), b'\x80\x02\x88.')
    BoolTest.assertEqual(pickle.dumps(False, protocol=2), b'\x80\x02\x89.')

BoolTest = test_bool.BoolTest()
test_picklevalues()
