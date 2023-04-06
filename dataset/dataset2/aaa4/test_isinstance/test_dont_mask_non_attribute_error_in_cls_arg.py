import unittest
import sys
import typing
import test_isinstance

def test_dont_mask_non_attribute_error_in_cls_arg():

    class B:
        pass

    class C(object):

        def getbases(TestIsSubclassExceptions):
            raise RuntimeError
        __bases__ = property(getbases)
    TestIsSubclassExceptions.assertRaises(RuntimeError, issubclass, B, C())

TestIsSubclassExceptions = test_isinstance.TestIsSubclassExceptions()
test_dont_mask_non_attribute_error_in_cls_arg()
