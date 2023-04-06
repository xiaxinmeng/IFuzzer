from collections import UserList
from test import list_tests
import unittest
import test_userlist

def test_mixedcmp():
    u = UserListTest.type2test([0, 1])
    UserListTest.assertEqual(u, [0, 1])
    UserListTest.assertNotEqual(u, [0])
    UserListTest.assertNotEqual(u, [0, 2])

UserListTest = test_userlist.UserListTest()
test_mixedcmp()
