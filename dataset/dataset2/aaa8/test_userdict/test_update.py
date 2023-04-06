from test import mapping_tests
import unittest
import collections
import test_userdict

def test_update():
    for kw in ('UserDictTest', 'dict', 'other', 'iterable'):
        d = collections.UserDict()
        d.update(**{kw: 42})
        UserDictTest.assertEqual(list(d.items()), [(kw, 42)])
    UserDictTest.assertRaises(TypeError, collections.UserDict().update, 42)
    UserDictTest.assertRaises(TypeError, collections.UserDict().update, {}, {})
    UserDictTest.assertRaises(TypeError, collections.UserDict.update)

UserDictTest = test_userdict.UserDictTest()
test_update()
