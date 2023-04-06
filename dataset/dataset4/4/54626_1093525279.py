# -*- coding: utf-8 -*-
import unittest

class UnicodeTest(unittest.TestCase):
    def test_unicode_docstring(self):
        u"""täst - docstring with unicode character"""
        self.assertEqual(1+1, 2)

if __name__ == '__main__':
    unittest.main()