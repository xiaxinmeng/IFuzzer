import hashlib
from http.client import HTTPException
import sys
import unicodedata
import unittest
from test.support import open_urlresource, requires_resource, script_helper
import unicodedata
import test_unicodedata

def test_bug_1704793():
    UnicodeMiscTest.assertEqual(UnicodeMiscTest.db.lookup('GOTHIC LETTER FAIHU'), '𐍆')

UnicodeMiscTest = test_unicodedata.UnicodeMiscTest()
test_bug_1704793()
