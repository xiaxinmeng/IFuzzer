import types
import unittest
import test_subclassinit

def test_type():
    t = type('NewClass', (object,), {})
    Test.assertIsInstance(t, type)
    Test.assertEqual(t.__name__, 'NewClass')
    with Test.assertRaises(TypeError):
        type(name='NewClass', bases=(object,), dict={})

Test = test_subclassinit.Test()
test_type()
