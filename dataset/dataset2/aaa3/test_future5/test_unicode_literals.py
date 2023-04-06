from __future__ import unicode_literals, print_function
import sys
import unittest
from test import support
import test_future5

def test_unicode_literals():
    TestMultipleFeatures.assertIsInstance('', str)

TestMultipleFeatures = test_future5.TestMultipleFeatures()
test_unicode_literals()
