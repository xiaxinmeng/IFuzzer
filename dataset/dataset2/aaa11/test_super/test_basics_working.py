import unittest
import test_super

def test_basics_working():
    TestSuper.assertEqual(test_super.D().f(), 'ABCD')

TestSuper = test_super.TestSuper()
test_basics_working()
