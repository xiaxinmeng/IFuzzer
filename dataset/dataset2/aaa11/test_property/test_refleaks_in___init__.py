import sys
import unittest
from test import support
import test_property

@support.refcount_test
def test_refleaks_in___init__():
    gettotalrefcount = support.get_attribute(sys, 'gettotalrefcount')
    fake_prop = property('fget', 'fset', 'fdel', 'doc')
    refs_before = gettotalrefcount()
    for i in range(100):
        fake_prop.__init__('fget', 'fset', 'fdel', 'doc')
    PropertyTests.assertAlmostEqual(gettotalrefcount() - refs_before, 0, delta=10)

PropertyTests = test_property.PropertyTests()
test_refleaks_in___init__()
