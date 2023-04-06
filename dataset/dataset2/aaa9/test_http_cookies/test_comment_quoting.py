import copy
from test.support import run_unittest, run_doctest
import unittest
from http import cookies
import pickle
import test_http_cookies

def test_comment_quoting():
    c = cookies.SimpleCookie()
    c['foo'] = '©'
    CookieTests.assertEqual(str(c['foo']), 'Set-Cookie: foo="\\251"')
    c['foo']['comment'] = 'comment ©'
    CookieTests.assertEqual(str(c['foo']), 'Set-Cookie: foo="\\251"; Comment="comment \\251"')

CookieTests = test_http_cookies.CookieTests()
test_comment_quoting()
