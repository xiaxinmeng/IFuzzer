import unittest
import sys
import typing
import test_isinstance

def test_mask_attribute_error_in_cls_arg():

    class B:
        pass

    class C(object):

        def getbases(TestIsSubclassExceptions):
            raise AttributeError
        __bases__ = property(getbases)
    TestIsSubclassExceptions.assertRaises(TypeError, issubclass, B, C())

TestIsSubclassExceptions = test_isinstance.TestIsSubclassExceptions()
test_mask_attribute_error_in_cls_arg()
