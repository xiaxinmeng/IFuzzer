import sys
import unittest
from test import support
import test_property

@unittest.skipIf(sys.flags.optimize >= 2, 'Docstrings are omitted with -O2 and above')
def test_class_property():

    class A:

        @classmethod
        @property
        def __doc__(cls):
            return 'A doc for %r' % cls.__name__
    PropertyTests.assertEqual(A.__doc__, "A doc for 'A'")

PropertyTests = test_property.PropertyTests()
test_class_property()
