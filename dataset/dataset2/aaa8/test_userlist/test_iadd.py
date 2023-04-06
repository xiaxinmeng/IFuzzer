from collections import UserList
from test import list_tests
import unittest
import test_userlist

def test_iadd():
    super().test_iadd()
    u = [0, 1]
    u += UserList([0, 1])
    UserListTest.assertEqual(u, [0, 1, 0, 1])

UserListTest = test_userlist.UserListTest()
test_iadd()
