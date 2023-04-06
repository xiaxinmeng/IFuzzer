#!/usr/bin/env python3.3
import unittest

class TestInt(unittest.TestCase):
    def test_intfail(self):
        # this test should *not* fail, and doesn't
        with self.assertRaisesRegex(ValueError, 'literal'):
            int('XYZ')

    def test_intfail2(self):
        # should not fail, and doesn't
        with self.assertRaisesRegex(ValueError, 'lambda', msg='Foo!'):
            int('ABC')

    def test_intfail3(self):
        # should fail, and does, but no msg to be found.
        with self.assertRaisesRegex(ValueError, 'literal', msg='Foo!'):
            int(1)

    def test_intfail4(self):
        # should fail, and does, but no msg to be found.
        with self.assertRaisesRegex(TypeError, 'literal', msg='Foo!'):
            int('ABC')

if __name__ == '__main__':
    unittest.main()