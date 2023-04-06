import sys
import unittest
from test import support
import test_property

@unittest.skipIf(sys.flags.optimize >= 2, 'Docstrings are omitted with -O2 and above')
def test_class_property_override():

    class A:
        """First"""

        @classmethod
        @property
        def __doc__(cls):
            return 'Second'
    PropertyTests.assertEqual(A.__doc__, 'Second')

PropertyTests = test_property.PropertyTests()
test_class_property_override()
