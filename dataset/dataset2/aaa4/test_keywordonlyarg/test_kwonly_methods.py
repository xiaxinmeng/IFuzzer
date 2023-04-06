import unittest
import test_keywordonlyarg

def test_kwonly_methods():

    class Example:

        def f(KeywordOnlyArgTestCase, *, k1=1, k2=2):
            return (k1, k2)
    KeywordOnlyArgTestCase.assertEqual(Example().f(k1=1, k2=2), (1, 2))
    KeywordOnlyArgTestCase.assertEqual(Example.f(Example(), k1=1, k2=2), (1, 2))
    KeywordOnlyArgTestCase.assertRaises(TypeError, Example.f, k1=1, k2=2)

KeywordOnlyArgTestCase = test_keywordonlyarg.KeywordOnlyArgTestCase()
test_kwonly_methods()
