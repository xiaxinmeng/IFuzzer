import linecache
import unittest
import os.path
import tempfile
import tokenize
from test import support
from test.support import os_helper
import test_linecache

def test_no_ending_newline():
    LineCacheTests.addCleanup(os_helper.unlink, os_helper.TESTFN)
    with open(os_helper.TESTFN, 'w') as fp:
        fp.write(test_linecache.SOURCE_3)
    lines = linecache.getlines(os_helper.TESTFN)
    LineCacheTests.assertEqual(lines, ['\n', 'def f():\n', '    return 3\n'])

LineCacheTests = test_linecache.LineCacheTests()
test_no_ending_newline()
