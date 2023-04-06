import unittest
import test_super

def test_class_methods_still_working():
    TestSuper.assertEqual(test_super.A.cm(), (test_super.A, 'A'))
    TestSuper.assertEqual(test_super.A().cm(), (test_super.A, 'A'))
    TestSuper.assertEqual(test_super.G.cm(), (test_super.G, 'A'))
    TestSuper.assertEqual(test_super.G().cm(), (test_super.G, 'A'))

TestSuper = test_super.TestSuper()
test_class_methods_still_working()
