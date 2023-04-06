import unittest
import test_super

def test_super_with_closure():

    class E(test_super.A):

        def f(TestSuper):

            def nested():
                TestSuper
            return super().f() + 'E'
    TestSuper.assertEqual(test_super.E().f(), 'AE')

TestSuper = test_super.TestSuper()
test_super_with_closure()
