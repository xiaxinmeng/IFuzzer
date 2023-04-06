import copy
from test.support import run_unittest, run_doctest
import unittest
from http import cookies
import pickle
import test_http_cookies

def test_set_properties():
    morsel = cookies.Morsel()
    with MorselTests.assertRaises(AttributeError):
        morsel.key = ''
    with MorselTests.assertRaises(AttributeError):
        morsel.value = ''
    with MorselTests.assertRaises(AttributeError):
        morsel.coded_value = ''

MorselTests = test_http_cookies.MorselTests()
test_set_properties()
