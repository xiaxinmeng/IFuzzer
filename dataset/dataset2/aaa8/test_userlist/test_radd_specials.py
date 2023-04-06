from collections import UserList
from test import list_tests
import unittest
import test_userlist

def test_radd_specials():
    u = UserList('eggs')
    u2 = 'spam' + u
    UserListTest.assertEqual(u2, list('spameggs'))
    u2 = u.__radd__(UserList('spam'))
    UserListTest.assertEqual(u2, list('spameggs'))

UserListTest = test_userlist.UserListTest()
test_radd_specials()
