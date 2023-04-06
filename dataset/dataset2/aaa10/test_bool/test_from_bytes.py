import unittest
from test import support
from test.support import os_helper
import os
import operator
import marshal
import pickle
import pickle
import test_bool

def test_from_bytes():
    BoolTest.assertIs(bool.from_bytes(b'\x00' * 8, 'big'), False)
    BoolTest.assertIs(bool.from_bytes(b'abcd', 'little'), True)

BoolTest = test_bool.BoolTest()
test_from_bytes()
