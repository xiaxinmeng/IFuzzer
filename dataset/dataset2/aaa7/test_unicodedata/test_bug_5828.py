import hashlib
from http.client import HTTPException
import sys
import unicodedata
import unittest
from test.support import open_urlresource, requires_resource, script_helper
import unicodedata
import test_unicodedata

def test_bug_5828():
    UnicodeMiscTest.assertEqual('ᵹ'.lower(), 'ᵹ')
    UnicodeMiscTest.assertEqual([c for c in range(sys.maxunicode + 1) if '\x00' in chr(c).lower() + chr(c).upper() + chr(c).title()], [0])

UnicodeMiscTest = test_unicodedata.UnicodeMiscTest()
test_bug_5828()
