import linecache
import unittest
import os.path
import tempfile
import tokenize
from test import support
from test.support import os_helper
import test_linecache

def test_lazycache_no_globals():
    lines = linecache.getlines(test_linecache.FILENAME)
    linecache.clearcache()
    LineCacheTests.assertEqual(False, linecache.lazycache(test_linecache.FILENAME, None))
    LineCacheTests.assertEqual(lines, linecache.getlines(test_linecache.FILENAME))

LineCacheTests = test_linecache.LineCacheTests()
test_lazycache_no_globals()
