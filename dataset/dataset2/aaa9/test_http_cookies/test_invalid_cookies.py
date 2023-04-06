import copy
from test.support import run_unittest, run_doctest
import unittest
from http import cookies
import pickle
import test_http_cookies

def test_invalid_cookies():
    C = cookies.SimpleCookie()
    for s in (']foo=x', '[foo=x', 'blah]foo=x', 'blah[foo=x', 'Set-Cookie: foo=bar', 'Set-Cookie: foo', 'foo=bar; baz', 'baz; foo=bar', 'secure;foo=bar', 'Version=1;foo=bar'):
        C.load(s)
        CookieTests.assertEqual(dict(C), {})
        CookieTests.assertEqual(C.output(), '')

CookieTests = test_http_cookies.CookieTests()
test_invalid_cookies()
