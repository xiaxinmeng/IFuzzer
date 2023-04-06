import copy
from test.support import run_unittest, run_doctest
import unittest
from http import cookies
import pickle
import test_http_cookies

def test_extended_encode():
    C = cookies.SimpleCookie()
    C['val'] = 'some,funky;stuff'
    CookieTests.assertEqual(C.output(['val']), 'Set-Cookie: val="some\\054funky\\073stuff"')

CookieTests = test_http_cookies.CookieTests()
test_extended_encode()
