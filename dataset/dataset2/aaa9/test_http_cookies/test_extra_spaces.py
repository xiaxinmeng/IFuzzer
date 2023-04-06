import copy
from test.support import run_unittest, run_doctest
import unittest
from http import cookies
import pickle
import test_http_cookies

def test_extra_spaces():
    C = cookies.SimpleCookie()
    C.load('eggs  =  scrambled  ;  secure  ;  path  =  bar   ; foo=foo   ')
    CookieTests.assertEqual(C.output(), 'Set-Cookie: eggs=scrambled; Path=bar; Secure\r\nSet-Cookie: foo=foo')

CookieTests = test_http_cookies.CookieTests()
test_extra_spaces()
