import unittest
import test_super

def test_super_in_class_methods_working():
    d = test_super.D()
    TestSuper.assertEqual(d.cm(), (d, (test_super.D, (test_super.D, (test_super.D, 'A'), 'B'), 'C'), 'D'))
    e = test_super.E()
    TestSuper.assertEqual(e.cm(), (e, (test_super.E, (test_super.E, (test_super.E, 'A'), 'B'), 'C'), 'D'))

TestSuper = test_super.TestSuper()
test_super_in_class_methods_working()
