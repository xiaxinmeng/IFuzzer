import hashlib
from http.client import HTTPException
import sys
import unicodedata
import unittest
from test.support import open_urlresource, requires_resource, script_helper
import unicodedata
import test_unicodedata

def test_decimal():
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.decimal('A', None), None)
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.decimal('9'), 9)
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.decimal('⅛', None), None)
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.decimal('⑨', None), None)
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.decimal('𠀀', None), None)
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.decimal('𝟽'), 7)
    UnicodeFunctionsTest.assertRaises(TypeError, UnicodeFunctionsTest.db.decimal)
    UnicodeFunctionsTest.assertRaises(TypeError, UnicodeFunctionsTest.db.decimal, 'xx')
    UnicodeFunctionsTest.assertRaises(ValueError, UnicodeFunctionsTest.db.decimal, 'x')

UnicodeFunctionsTest = test_unicodedata.UnicodeFunctionsTest()
test_decimal()
