import copy
from test.support import run_unittest, run_doctest
import unittest
from http import cookies
import pickle
import test_http_cookies

def test_setitem():
    morsel = cookies.Morsel()
    morsel['expires'] = 0
    MorselTests.assertEqual(morsel['expires'], 0)
    morsel['Version'] = 2
    MorselTests.assertEqual(morsel['version'], 2)
    morsel['DOMAIN'] = 'example.com'
    MorselTests.assertEqual(morsel['domain'], 'example.com')
    with MorselTests.assertRaises(cookies.CookieError):
        morsel['invalid'] = 'value'
    MorselTests.assertNotIn('invalid', morsel)

MorselTests = test_http_cookies.MorselTests()
test_setitem()
