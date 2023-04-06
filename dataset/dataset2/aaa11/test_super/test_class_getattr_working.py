import unittest
import test_super

def test_class_getattr_working():
    TestSuper.assertEqual(test_super.D.f(test_super.D()), 'ABCD')

TestSuper = test_super.TestSuper()
test_class_getattr_working()
