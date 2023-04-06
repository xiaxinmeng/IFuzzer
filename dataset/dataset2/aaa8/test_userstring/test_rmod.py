import unittest
from test import string_tests
from collections import UserString
import test_userstring

def test_rmod():

    class ustr2(UserString):
        pass

    class ustr3(ustr2):

        def __rmod__(UserStringTest, other):
            return super().__rmod__(other)
    fmt2 = ustr2('value is %s')
    str3 = ustr3('TEST')
    UserStringTest.assertEqual(fmt2 % str3, 'value is TEST')

UserStringTest = test_userstring.UserStringTest()
test_rmod()
