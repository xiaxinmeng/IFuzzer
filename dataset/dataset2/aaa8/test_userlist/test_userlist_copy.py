from collections import UserList
from test import list_tests
import unittest
import test_userlist

def test_userlist_copy():
    u = UserListTest.type2test([6, 8, 1, 9, 1])
    v = u.copy()
    UserListTest.assertEqual(u, v)
    UserListTest.assertEqual(type(u), type(v))

UserListTest = test_userlist.UserListTest()
test_userlist_copy()
