import hashlib
from http.client import HTTPException
import sys
import unicodedata
import unittest
from test.support import open_urlresource, requires_resource, script_helper
import unicodedata
import test_unicodedata

def test_issue10254():
    a = 'C̸' * 20 + 'Ç'
    b = 'C̸' * 20 + 'Ç'
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.normalize('NFC', a), b)

UnicodeFunctionsTest = test_unicodedata.UnicodeFunctionsTest()
test_issue10254()
