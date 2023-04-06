import copy
from test.support import run_unittest, run_doctest
import unittest
from http import cookies
import pickle
import test_http_cookies

def test_special_attrs():
    C = cookies.SimpleCookie('Customer="WILE_E_COYOTE"')
    C['Customer']['expires'] = 0
    CookieTests.assertTrue(C.output().endswith('GMT'))
    C = cookies.SimpleCookie()
    C.load('Customer="W"; expires=Wed, 01 Jan 2010 00:00:00 GMT')
    CookieTests.assertEqual(C['Customer']['expires'], 'Wed, 01 Jan 2010 00:00:00 GMT')
    C = cookies.SimpleCookie()
    C.load('Customer="W"; expires=Wed, 01 Jan 98 00:00:00 GMT')
    CookieTests.assertEqual(C['Customer']['expires'], 'Wed, 01 Jan 98 00:00:00 GMT')
    C = cookies.SimpleCookie('Customer="WILE_E_COYOTE"')
    C['Customer']['max-age'] = 10
    CookieTests.assertEqual(C.output(), 'Set-Cookie: Customer="WILE_E_COYOTE"; Max-Age=10')

CookieTests = test_http_cookies.CookieTests()
test_special_attrs()
