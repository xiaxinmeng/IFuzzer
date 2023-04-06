from collections import UserList
from test import list_tests
import unittest
import test_userlist

def test_getitemoverwriteiter():

    class T(UserListTest.type2test):

        def __getitem__(UserListTest, key):
            return str(key) + '!!!'
    UserListTest.assertEqual(next(iter(T((1, 2)))), '0!!!')

UserListTest = test_userlist.UserListTest()
test_getitemoverwriteiter()
