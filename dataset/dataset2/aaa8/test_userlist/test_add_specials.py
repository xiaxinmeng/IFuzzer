from collections import UserList
from test import list_tests
import unittest
import test_userlist

def test_add_specials():
    u = UserList('spam')
    u2 = u + 'eggs'
    UserListTest.assertEqual(u2, list('spameggs'))

UserListTest = test_userlist.UserListTest()
test_add_specials()
