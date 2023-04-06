import copy
from test.support import run_unittest, run_doctest
import unittest
from http import cookies
import pickle
import test_http_cookies

def test_setdefault():
    morsel = cookies.Morsel()
    morsel.update({'domain': 'example.com', 'version': 2})
    MorselTests.assertEqual(morsel.setdefault('expires', 'value'), '')
    MorselTests.assertEqual(morsel['expires'], '')
    MorselTests.assertEqual(morsel.setdefault('Version', 1), 2)
    MorselTests.assertEqual(morsel['version'], 2)
    MorselTests.assertEqual(morsel.setdefault('DOMAIN', 'value'), 'example.com')
    MorselTests.assertEqual(morsel['domain'], 'example.com')
    with MorselTests.assertRaises(cookies.CookieError):
        morsel.setdefault('invalid', 'value')
    MorselTests.assertNotIn('invalid', morsel)

MorselTests = test_http_cookies.MorselTests()
test_setdefault()
