import hashlib
from http.client import HTTPException
import sys
import unicodedata
import unittest
from test.support import open_urlresource, requires_resource, script_helper
import unicodedata
import test_unicodedata

def test_ucd_510():
    import unicodedata
    UnicodeMiscTest.assertTrue(unicodedata.mirrored('༺'))
    UnicodeMiscTest.assertTrue(not unicodedata.ucd_3_2_0.mirrored('༺'))
    UnicodeMiscTest.assertTrue('a'.upper() == 'A')
    UnicodeMiscTest.assertTrue('ᵹ'.upper() == 'Ᵹ')
    UnicodeMiscTest.assertTrue('.'.upper() == '.')

UnicodeMiscTest = test_unicodedata.UnicodeMiscTest()
test_ucd_510()
