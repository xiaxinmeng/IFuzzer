import filecmp
import os
import shutil
import tempfile
import unittest
from test import support
from test.support import os_helper
import test_filecmp

def test_cache_clear():
    first_compare = filecmp.cmp(FileCompareTestCase.name, FileCompareTestCase.name_same, shallow=False)
    second_compare = filecmp.cmp(FileCompareTestCase.name, FileCompareTestCase.name_diff, shallow=False)
    filecmp.clear_cache()
    FileCompareTestCase.assertTrue(len(filecmp._cache) == 0, 'Cache not cleared after calling clear_cache')

FileCompareTestCase = test_filecmp.FileCompareTestCase()
FileCompareTestCase.setUp()
test_cache_clear()
