import hashlib
from http.client import HTTPException
import sys
import unicodedata
import unittest
from test.support import open_urlresource, requires_resource, script_helper
import unicodedata
import test_unicodedata

def test_failed_import_during_compiling():
    code = 'import sys;sys.modules[\'unicodedata\'] = None;eval("\'\\\\N{SOFT HYPHEN}\'")'
    result = script_helper.assert_python_failure('-c', code)
    error = "SyntaxError: (unicode error) \\N escapes not supported (can't load unicodedata module)"
    UnicodeMiscTest.assertIn(error, result.err.decode('ascii'))

UnicodeMiscTest = test_unicodedata.UnicodeMiscTest()
test_failed_import_during_compiling()
