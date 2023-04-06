import sys
from test import list_tests
from test.support import cpython_only
import pickle
import unittest
import test_list

def test_no_comdat_folding():

    class L(list):
        pass
    with ListTest.assertRaises(TypeError):
        (3,) + L([1, 2])

ListTest = test_list.ListTest()
test_no_comdat_folding()
