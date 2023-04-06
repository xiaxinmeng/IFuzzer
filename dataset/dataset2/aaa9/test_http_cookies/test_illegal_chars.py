import copy
from test.support import run_unittest, run_doctest
import unittest
from http import cookies
import pickle
import test_http_cookies

def test_illegal_chars():
    rawdata = 'a=b; c,d=e'
    C = cookies.SimpleCookie()
    with CookieTests.assertRaises(cookies.CookieError):
        C.load(rawdata)

CookieTests = test_http_cookies.CookieTests()
test_illegal_chars()
