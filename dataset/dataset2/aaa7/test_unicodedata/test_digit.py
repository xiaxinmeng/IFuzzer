import hashlib
from http.client import HTTPException
import sys
import unicodedata
import unittest
from test.support import open_urlresource, requires_resource, script_helper
import unicodedata
import test_unicodedata

def test_digit():
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.digit('A', None), None)
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.digit('9'), 9)
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.digit('⅛', None), None)
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.digit('⑨'), 9)
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.digit('𠀀', None), None)
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.digit('𝟽'), 7)
    UnicodeFunctionsTest.assertRaises(TypeError, UnicodeFunctionsTest.db.digit)
    UnicodeFunctionsTest.assertRaises(TypeError, UnicodeFunctionsTest.db.digit, 'xx')
    UnicodeFunctionsTest.assertRaises(ValueError, UnicodeFunctionsTest.db.digit, 'x')

UnicodeFunctionsTest = test_unicodedata.UnicodeFunctionsTest()
test_digit()
