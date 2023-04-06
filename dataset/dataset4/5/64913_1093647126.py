#!/usr/bin/env python
import unittest
import xmlrunner

class Foo(unittest.TestCase):
    def testFoo(self):
        self.assertTrue(False, ']]>')

unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))