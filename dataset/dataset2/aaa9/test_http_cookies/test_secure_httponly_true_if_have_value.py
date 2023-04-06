import copy
from test.support import run_unittest, run_doctest
import unittest
from http import cookies
import pickle
import test_http_cookies

def test_secure_httponly_true_if_have_value():
    C = cookies.SimpleCookie()
    C.load('eggs=scrambled; httponly=foo; secure=bar; Path=/bacon')
    CookieTests.assertTrue(C['eggs']['httponly'])
    CookieTests.assertTrue(C['eggs']['secure'])
    CookieTests.assertEqual(C['eggs']['httponly'], 'foo')
    CookieTests.assertEqual(C['eggs']['secure'], 'bar')

CookieTests = test_http_cookies.CookieTests()
test_secure_httponly_true_if_have_value()
