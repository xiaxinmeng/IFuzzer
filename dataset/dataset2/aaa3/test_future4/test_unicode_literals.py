from __future__ import unicode_literals
import unittest
import test_future4

def test_unicode_literals():
    Tests.assertIsInstance('literal', str)

Tests = test_future4.Tests()
test_unicode_literals()
