import linecache
import unittest
import os.path
import tempfile
import tokenize
from test import support
from test.support import os_helper
import test_linecache

def test_lazycache_check():
    linecache.clearcache()
    linecache.lazycache(test_linecache.NONEXISTENT_FILENAME, globals())
    linecache.checkcache()

LineCacheTests = test_linecache.LineCacheTests()
test_lazycache_check()
