import hashlib
from http.client import HTTPException
import sys
import unicodedata
import unittest
from test.support import open_urlresource, requires_resource, script_helper
import unicodedata
import test_unicodedata

def test_decomposition():
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.decomposition('\ufffe'), '')
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.decomposition('¼'), '<fraction> 0031 2044 0034')
    UnicodeFunctionsTest.assertRaises(TypeError, UnicodeFunctionsTest.db.decomposition)
    UnicodeFunctionsTest.assertRaises(TypeError, UnicodeFunctionsTest.db.decomposition, 'xx')

UnicodeFunctionsTest = test_unicodedata.UnicodeFunctionsTest()
test_decomposition()
