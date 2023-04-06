import unittest
import sys
import typing
import test_isinstance

def test_dont_mask_non_attribute_error():

    class C(object):

        def getbases(TestIsInstanceExceptions):
            raise RuntimeError
        __bases__ = property(getbases)

    class S(C):
        pass
    TestIsInstanceExceptions.assertRaises(RuntimeError, issubclass, C(), S())

TestIsInstanceExceptions = test_isinstance.TestIsInstanceExceptions()
test_dont_mask_non_attribute_error()
