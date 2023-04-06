import unittest
from test import string_tests
from collections import UserString
import test_userstring

def test_encode_default_args():
    UserStringTest.checkequal(b'hello', 'hello', 'encode')
    UserStringTest.checkequal(b'\xf0\xa3\x91\x96', '𣑖', 'encode')
    UserStringTest.checkraises(UnicodeError, '\ud800', 'encode')

UserStringTest = test_userstring.UserStringTest()
test_encode_default_args()
