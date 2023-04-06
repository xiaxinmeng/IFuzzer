import copy
from test.support import run_unittest, run_doctest
import unittest
from http import cookies
import pickle
import test_http_cookies

def test_set_secure_httponly_attrs():
    C = cookies.SimpleCookie('Customer="WILE_E_COYOTE"')
    C['Customer']['secure'] = True
    C['Customer']['httponly'] = True
    CookieTests.assertEqual(C.output(), 'Set-Cookie: Customer="WILE_E_COYOTE"; HttpOnly; Secure')

CookieTests = test_http_cookies.CookieTests()
test_set_secure_httponly_attrs()
