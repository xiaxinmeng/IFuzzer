import unittest
import test_super

def test_subclass_no_override_working():
    TestSuper.assertEqual(test_super.E().f(), 'ABCD')
    TestSuper.assertEqual(test_super.E.f(test_super.E()), 'ABCD')

TestSuper = test_super.TestSuper()
test_subclass_no_override_working()
