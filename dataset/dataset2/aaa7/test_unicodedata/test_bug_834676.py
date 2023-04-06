import hashlib
from http.client import HTTPException
import sys
import unicodedata
import unittest
from test.support import open_urlresource, requires_resource, script_helper
import unicodedata
import test_unicodedata

def test_bug_834676():
    unicodedata.normalize('NFC', '한글')

NormalizationTest = test_unicodedata.NormalizationTest()
test_bug_834676()
