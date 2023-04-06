from test import mapping_tests
import unittest
import collections
import test_userdict

def test_init():
    for kw in ('UserDictTest', 'other', 'iterable'):
        UserDictTest.assertEqual(list(collections.UserDict(**{kw: 42}).items()), [(kw, 42)])
    UserDictTest.assertEqual(list(collections.UserDict({}, dict=42).items()), [('dict', 42)])
    UserDictTest.assertEqual(list(collections.UserDict({}, dict=None).items()), [('dict', None)])
    UserDictTest.assertEqual(list(collections.UserDict(dict={'a': 42}).items()), [('dict', {'a': 42})])
    UserDictTest.assertRaises(TypeError, collections.UserDict, 42)
    UserDictTest.assertRaises(TypeError, collections.UserDict, (), ())
    UserDictTest.assertRaises(TypeError, collections.UserDict.__init__)

UserDictTest = test_userdict.UserDictTest()
test_init()
