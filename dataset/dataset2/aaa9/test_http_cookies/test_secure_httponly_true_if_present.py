import copy
from test.support import run_unittest, run_doctest
import unittest
from http import cookies
import pickle
import test_http_cookies

def test_secure_httponly_true_if_present():
    C = cookies.SimpleCookie()
    C.load('eggs=scrambled; httponly; secure; Path=/bacon')
    CookieTests.assertTrue(C['eggs']['httponly'])
    CookieTests.assertTrue(C['eggs']['secure'])

CookieTests = test_http_cookies.CookieTests()
test_secure_httponly_true_if_present()
