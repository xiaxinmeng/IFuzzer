import hashlib
from http.client import HTTPException
import sys
import unicodedata
import unittest
from test.support import open_urlresource, requires_resource, script_helper
import unicodedata
import test_unicodedata

def test_combining():
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.combining('\ufffe'), 0)
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.combining('a'), 0)
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.combining('⃡'), 230)
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.combining('𠀀'), 0)
    UnicodeFunctionsTest.assertRaises(TypeError, UnicodeFunctionsTest.db.combining)
    UnicodeFunctionsTest.assertRaises(TypeError, UnicodeFunctionsTest.db.combining, 'xx')

UnicodeFunctionsTest = test_unicodedata.UnicodeFunctionsTest()
test_combining()
