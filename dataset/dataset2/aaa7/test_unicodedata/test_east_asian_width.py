import hashlib
from http.client import HTTPException
import sys
import unicodedata
import unittest
from test.support import open_urlresource, requires_resource, script_helper
import unicodedata
import test_unicodedata

def test_east_asian_width():
    eaw = UnicodeFunctionsTest.db.east_asian_width
    UnicodeFunctionsTest.assertRaises(TypeError, eaw, b'a')
    UnicodeFunctionsTest.assertRaises(TypeError, eaw, bytearray())
    UnicodeFunctionsTest.assertRaises(TypeError, eaw, '')
    UnicodeFunctionsTest.assertRaises(TypeError, eaw, 'ra')
    UnicodeFunctionsTest.assertEqual(eaw('\x1e'), 'N')
    UnicodeFunctionsTest.assertEqual(eaw(' '), 'Na')
    UnicodeFunctionsTest.assertEqual(eaw('좔'), 'W')
    UnicodeFunctionsTest.assertEqual(eaw('ｦ'), 'H')
    UnicodeFunctionsTest.assertEqual(eaw('？'), 'F')
    UnicodeFunctionsTest.assertEqual(eaw('‐'), 'A')
    UnicodeFunctionsTest.assertEqual(eaw('𠀀'), 'W')

UnicodeFunctionsTest = test_unicodedata.UnicodeFunctionsTest()
test_east_asian_width()
