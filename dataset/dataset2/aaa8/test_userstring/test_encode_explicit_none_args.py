import unittest
from test import string_tests
from collections import UserString
import test_userstring

def test_encode_explicit_none_args():
    UserStringTest.checkequal(b'hello', 'hello', 'encode', None, None)
    UserStringTest.checkequal(b'\xf0\xa3\x91\x96', '𣑖', 'encode', None, None)
    UserStringTest.checkraises(UnicodeError, '\ud800', 'encode', None, None)

UserStringTest = test_userstring.UserStringTest()
test_encode_explicit_none_args()
