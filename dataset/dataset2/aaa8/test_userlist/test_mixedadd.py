from collections import UserList
from test import list_tests
import unittest
import test_userlist

def test_mixedadd():
    u = UserListTest.type2test([0, 1])
    UserListTest.assertEqual(u + [], u)
    UserListTest.assertEqual(u + [2], [0, 1, 2])

UserListTest = test_userlist.UserListTest()
test_mixedadd()
