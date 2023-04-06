import copy
from test.support import run_unittest, run_doctest
import unittest
from http import cookies
import pickle
import test_http_cookies

def test_defaults():
    morsel = cookies.Morsel()
    MorselTests.assertIsNone(morsel.key)
    MorselTests.assertIsNone(morsel.value)
    MorselTests.assertIsNone(morsel.coded_value)
    MorselTests.assertEqual(morsel.keys(), cookies.Morsel._reserved.keys())
    for (key, val) in morsel.items():
        MorselTests.assertEqual(val, '', key)

MorselTests = test_http_cookies.MorselTests()
test_defaults()
