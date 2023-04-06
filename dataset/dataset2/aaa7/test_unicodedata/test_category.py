import hashlib
from http.client import HTTPException
import sys
import unicodedata
import unittest
from test.support import open_urlresource, requires_resource, script_helper
import unicodedata
import test_unicodedata

def test_category():
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.category('\ufffe'), 'Cn')
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.category('a'), 'Ll')
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.category('A'), 'Lu')
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.category('𠀀'), 'Lo')
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.category('𐄪'), 'No')
    UnicodeFunctionsTest.assertRaises(TypeError, UnicodeFunctionsTest.db.category)
    UnicodeFunctionsTest.assertRaises(TypeError, UnicodeFunctionsTest.db.category, 'xx')

UnicodeFunctionsTest = test_unicodedata.UnicodeFunctionsTest()
test_category()
