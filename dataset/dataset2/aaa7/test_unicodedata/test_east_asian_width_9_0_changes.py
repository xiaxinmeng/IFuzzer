import hashlib
from http.client import HTTPException
import sys
import unicodedata
import unittest
from test.support import open_urlresource, requires_resource, script_helper
import unicodedata
import test_unicodedata

def test_east_asian_width_9_0_changes():
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.ucd_3_2_0.east_asian_width('⌚'), 'N')
    UnicodeFunctionsTest.assertEqual(UnicodeFunctionsTest.db.east_asian_width('⌚'), 'W')

UnicodeFunctionsTest = test_unicodedata.UnicodeFunctionsTest()
test_east_asian_width_9_0_changes()
