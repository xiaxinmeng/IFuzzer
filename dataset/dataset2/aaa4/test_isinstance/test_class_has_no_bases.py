import unittest
import sys
import typing
import test_isinstance

def test_class_has_no_bases():

    class I(object):

        def getclass(TestIsInstanceExceptions):
            return None
        __class__ = property(getclass)

    class C(object):

        def getbases(TestIsInstanceExceptions):
            return ()
        __bases__ = property(getbases)
    TestIsInstanceExceptions.assertEqual(False, isinstance(I(), C()))

TestIsInstanceExceptions = test_isinstance.TestIsInstanceExceptions()
test_class_has_no_bases()
