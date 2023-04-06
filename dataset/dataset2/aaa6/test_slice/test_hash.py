import itertools
import operator
import sys
import unittest
import weakref
from pickle import loads, dumps
from test import support
import test_slice

def test_hash():
    SliceTest.assertRaises(TypeError, hash, slice(5))
    with SliceTest.assertRaises(TypeError):
        slice(5).__hash__()

SliceTest = test_slice.SliceTest()
test_hash()
