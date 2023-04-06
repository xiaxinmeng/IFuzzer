import linecache
import unittest
import os.path
import tempfile
import tokenize
from test import support
from test.support import os_helper
import test_linecache

def test_lazycache_bad_filename():
    linecache.clearcache()
    LineCacheTests.assertEqual(False, linecache.lazycache('', globals()))
    LineCacheTests.assertEqual(False, linecache.lazycache('<foo>', globals()))

LineCacheTests = test_linecache.LineCacheTests()
test_lazycache_bad_filename()
