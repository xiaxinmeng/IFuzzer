import hashlib
from http.client import HTTPException
import sys
import unicodedata
import unittest
from test.support import open_urlresource, requires_resource, script_helper
import unicodedata
import test_unicodedata

def test_mirrored():
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.mirrored('\ufffe'), 0)
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.mirrored('a'), 0)
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.mirrored('∁'), 1)
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.mirrored('𠀀'), 0)
    UnicodeFunctionsTest.assertRaises(TypeError, UnicodeFunctionsTest.db.mirrored)
    UnicodeFunctionsTest.assertRaises(TypeError, UnicodeFunctionsTest.db.mirrored, 'xx')

UnicodeFunctionsTest = test_unicodedata.UnicodeFunctionsTest()
test_mirrored()
