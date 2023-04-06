import hashlib
from http.client import HTTPException
import sys
import unicodedata
import unittest
from test.support import open_urlresource, requires_resource, script_helper
import unicodedata
import test_unicodedata

def test_bidirectional():
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.bidirectional('\ufffe'), '')
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.bidirectional(' '), 'WS')
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.bidirectional('A'), 'L')
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.bidirectional('𠀀'), 'L')
    UnicodeFunctionsTest.assertRaises(TypeError, UnicodeFunctionsTest.db.bidirectional)
    UnicodeFunctionsTest.assertRaises(TypeError, UnicodeFunctionsTest.db.bidirectional, 'xx')

UnicodeFunctionsTest = test_unicodedata.UnicodeFunctionsTest()
test_bidirectional()
