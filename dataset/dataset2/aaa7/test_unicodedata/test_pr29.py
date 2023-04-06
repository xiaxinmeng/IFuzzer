import hashlib
from http.client import HTTPException
import sys
import unicodedata
import unittest
from test.support import open_urlresource, requires_resource, script_helper
import unicodedata
import test_unicodedata

def test_pr29():
    composed = ('େ̀ା', 'ᄀ̀ᅡ', 'Li̍t-sṳ́', 'मार्क ज़' + 'ुकेरबर्ग', 'किर्गिज़' + 'स्तान')
    for text in composed:
        UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.normalize('NFC', text), text)

UnicodeFunctionsTest = test_unicodedata.UnicodeFunctionsTest()
test_pr29()
