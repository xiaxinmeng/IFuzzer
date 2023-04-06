import abc
import sys
import unittest
from types import DynamicClassAttribute
import test_dynamicclassattribute

@unittest.skipIf(hasattr(test_dynamicclassattribute.PropertySubSlots, '__doc__'), '__doc__ is already present, __slots__ will have no effect')
def test_slots_docstring_copy_exception():
    try:

        class Foo(object):

            @test_dynamicclassattribute.PropertySubSlots
            def spam(PropertySubclassTests):
                """Trying to copy this docstring will raise an exception"""
                return 1
            print('\n', spam.__doc__)
    except AttributeError:
        pass
    else:
        raise Exception('AttributeError not raised')

PropertySubclassTests = test_dynamicclassattribute.PropertySubclassTests()
test_slots_docstring_copy_exception()
