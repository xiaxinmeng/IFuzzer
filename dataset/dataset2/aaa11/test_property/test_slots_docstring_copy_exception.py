import sys
import unittest
from test import support
import test_property

def test_slots_docstring_copy_exception():
    try:

        class Foo(object):

            @test_property.PropertySubSlots
            def spam(PropertySubclassTests):
                """Trying to copy this docstring will raise an exception"""
                return 1
    except AttributeError:
        pass
    else:
        raise Exception('AttributeError not raised')

PropertySubclassTests = test_property.PropertySubclassTests()
test_slots_docstring_copy_exception()
