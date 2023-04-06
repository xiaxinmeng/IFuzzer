import linecache
import unittest
import os.path
import tempfile
import tokenize
from test import support
from test.support import os_helper
import test_linecache

def test_getlines():
    GetLineTestsGoodData.assertRaises((SyntaxError, UnicodeDecodeError), linecache.getlines, GetLineTestsGoodData.file_name)

GetLineTestsGoodData = test_linecache.GetLineTestsGoodData()
GetLineTestsGoodData.setUp()
test_getlines()
