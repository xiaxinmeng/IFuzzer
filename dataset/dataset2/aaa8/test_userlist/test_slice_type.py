from collections import UserList
from test import list_tests
import unittest
import test_userlist

def test_slice_type():
    l = [0, 1, 2, 3, 4]
    u = UserList(l)
    UserListTest.assertIsInstance(u[:], u.__class__)
    UserListTest.assertEqual(u[:], u)

UserListTest = test_userlist.UserListTest()
test_slice_type()
