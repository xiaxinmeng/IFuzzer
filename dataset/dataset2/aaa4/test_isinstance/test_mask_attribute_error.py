import unittest
import sys
import typing
import test_isinstance

def test_mask_attribute_error():

    class C(object):

        def getbases(TestIsInstanceExceptions):
            raise AttributeError
        __bases__ = property(getbases)

    class S(C):
        pass
    TestIsInstanceExceptions.assertRaises(TypeError, issubclass, C(), S())

TestIsInstanceExceptions = test_isinstance.TestIsInstanceExceptions()
test_mask_attribute_error()
