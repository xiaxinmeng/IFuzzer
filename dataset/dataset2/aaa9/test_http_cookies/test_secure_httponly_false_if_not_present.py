import copy
from test.support import run_unittest, run_doctest
import unittest
from http import cookies
import pickle
import test_http_cookies

def test_secure_httponly_false_if_not_present():
    C = cookies.SimpleCookie()
    C.load('eggs=scrambled; Path=/bacon')
    CookieTests.assertFalse(C['eggs']['httponly'])
    CookieTests.assertFalse(C['eggs']['secure'])

CookieTests = test_http_cookies.CookieTests()
test_secure_httponly_false_if_not_present()
