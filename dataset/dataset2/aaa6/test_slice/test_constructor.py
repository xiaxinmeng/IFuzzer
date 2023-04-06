import itertools
import operator
import sys
import unittest
import weakref
from pickle import loads, dumps
from test import support
import test_slice

def test_constructor():
    SliceTest.assertRaises(TypeError, slice)
    SliceTest.assertRaises(TypeError, slice, 1, 2, 3, 4)

SliceTest = test_slice.SliceTest()
test_constructor()
