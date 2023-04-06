import linecache
import unittest
import os.path
import tempfile
import tokenize
from test import support
from test.support import os_helper
import test_linecache

def test_lazycache_provide_after_failed_lookup():
    linecache.clearcache()
    lines = linecache.getlines(test_linecache.NONEXISTENT_FILENAME, globals())
    linecache.clearcache()
    linecache.getlines(test_linecache.NONEXISTENT_FILENAME)
    linecache.lazycache(test_linecache.NONEXISTENT_FILENAME, globals())
    LineCacheTests.assertEqual(lines, linecache.updatecache(test_linecache.NONEXISTENT_FILENAME))

LineCacheTests = test_linecache.LineCacheTests()
test_lazycache_provide_after_failed_lookup()
