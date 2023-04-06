import hashlib
from http.client import HTTPException
import sys
import unicodedata
import unittest
from test.support import open_urlresource, requires_resource, script_helper
import unicodedata
import test_unicodedata

def test_numeric():
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.numeric('A', None), None)
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.numeric('9'), 9)
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.numeric('⅛'), 0.125)
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.numeric('⑨'), 9.0)
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.numeric('꘧'), 7.0)
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.numeric('𠀀', None), None)
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.numeric('𐄪'), 9000)
    UnicodeFunctionsTest.assertRaises(TypeError, UnicodeFunctionsTest.db.numeric)
    UnicodeFunctionsTest.assertRaises(TypeError, UnicodeFunctionsTest.db.numeric, 'xx')
    UnicodeFunctionsTest.assertRaises(ValueError, UnicodeFunctionsTest.db.numeric, 'x')

UnicodeFunctionsTest = test_unicodedata.UnicodeFunctionsTest()
test_numeric()
