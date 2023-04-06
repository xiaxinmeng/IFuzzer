import filecmp
import os
import shutil
import tempfile
import unittest
from test import support
from test.support import os_helper
import test_filecmp

def test_dircmp_subdirs_type():
    """Check that dircmp.subdirs respects subclassing."""

    class MyDirCmp(filecmp.dircmp):
        pass
    d = MyDirCmp(DirCompareTestCase.dir, DirCompareTestCase.dir_diff)
    sub_dirs = d.subdirs
    DirCompareTestCase.assertEqual(list(sub_dirs.keys()), ['subdir'])
    sub_dcmp = sub_dirs['subdir']
    DirCompareTestCase.assertEqual(type(sub_dcmp), MyDirCmp)

DirCompareTestCase = test_filecmp.DirCompareTestCase()
DirCompareTestCase.setUp()
test_dircmp_subdirs_type()
