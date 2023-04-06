import hashlib
from http.client import HTTPException
import sys
import unicodedata
import unittest
from test.support import open_urlresource, requires_resource, script_helper
import unicodedata
import test_unicodedata

def test_linebreak_7643():
    for i in range(65536):
        lines = (chr(i) + 'A').splitlines()
        if i in (10, 11, 12, 13, 133, 28, 29, 30, 8232, 8233):
            UnicodeMiscTest.assertEqual(len(lines), 2, '\\u%.4x should be a linebreak' % i)
        else:
            UnicodeMiscTest.assertEqual(len(lines), 1, '\\u%.4x should not be a linebreak' % i)

UnicodeMiscTest = test_unicodedata.UnicodeMiscTest()
test_linebreak_7643()
