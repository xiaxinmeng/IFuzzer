import hashlib
from http.client import HTTPException
import sys
import unicodedata
import unittest
from test.support import open_urlresource, requires_resource, script_helper
import unicodedata
import test_unicodedata

def test_edge_cases():
    NormalizationTest.assertRaises(TypeError, unicodedata.normalize)
    NormalizationTest.assertRaises(ValueError, unicodedata.normalize, 'unknown', 'xx')
    NormalizationTest.assertEqual(unicodedata.normalize('NFKC', ''), '')

NormalizationTest = test_unicodedata.NormalizationTest()
test_edge_cases()
