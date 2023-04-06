import copy
import copyreg
import weakref
import abc
from operator import le, lt, ge, gt, eq, ne
import unittest
import test_copy

def test_getstate_exc():

    class EvilState(object):

        def __getstate__(TestCopy):
            raise ValueError("ain't got no stickin' state")
    TestCopy.assertRaises(ValueError, copy.copy, EvilState())

TestCopy = test_copy.TestCopy()
test_getstate_exc()
