import unittest
import test_super

def test_unbound_method_transfer_working():
    TestSuper.assertEqual(test_super.F().f(), 'ABCD')
    TestSuper.assertEqual(test_super.F.f(test_super.F()), 'ABCD')

TestSuper = test_super.TestSuper()
test_unbound_method_transfer_working()
