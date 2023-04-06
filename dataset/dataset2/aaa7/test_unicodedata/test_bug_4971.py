import hashlib
from http.client import HTTPException
import sys
import unicodedata
import unittest
from test.support import open_urlresource, requires_resource, script_helper
import unicodedata
import test_unicodedata

def test_bug_4971():
    UnicodeMiscTest.assertEqual('Ǆ'.title(), 'ǅ')
    UnicodeMiscTest.assertEqual('ǅ'.title(), 'ǅ')
    UnicodeMiscTest.assertEqual('ǆ'.title(), 'ǅ')

UnicodeMiscTest = test_unicodedata.UnicodeMiscTest()
test_bug_4971()
