import unittest
import test_keywordonlyarg

def test_mangling():

    class X:

        def f(KeywordOnlyArgTestCase, *, __a=42):
            return __a
    KeywordOnlyArgTestCase.assertEqual(X().f(), 42)

KeywordOnlyArgTestCase = test_keywordonlyarg.KeywordOnlyArgTestCase()
test_mangling()
