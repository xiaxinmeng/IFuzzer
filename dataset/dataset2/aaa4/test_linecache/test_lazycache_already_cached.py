import linecache
import unittest
import os.path
import tempfile
import tokenize
from test import support
from test.support import os_helper
import test_linecache

def test_lazycache_already_cached():
    linecache.clearcache()
    lines = linecache.getlines(test_linecache.NONEXISTENT_FILENAME, globals())
    LineCacheTests.assertEqual(False, linecache.lazycache(test_linecache.NONEXISTENT_FILENAME, globals()))
    LineCacheTests.assertEqual(4, len(linecache.cache[test_linecache.NONEXISTENT_FILENAME]))

LineCacheTests = test_linecache.LineCacheTests()
test_lazycache_already_cached()
