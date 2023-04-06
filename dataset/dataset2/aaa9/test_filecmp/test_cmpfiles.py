import filecmp
import os
import shutil
import tempfile
import unittest
from test import support
from test.support import os_helper
import test_filecmp

def test_cmpfiles():
    DirCompareTestCase.assertTrue(filecmp.cmpfiles(DirCompareTestCase.dir, DirCompareTestCase.dir, ['file']) == (['file'], [], []), 'Comparing directory to itDirCompareTestCase fails')
    DirCompareTestCase.assertTrue(filecmp.cmpfiles(DirCompareTestCase.dir, DirCompareTestCase.dir_same, ['file']) == (['file'], [], []), 'Comparing directory to same fails')
    DirCompareTestCase.assertTrue(filecmp.cmpfiles(DirCompareTestCase.dir, DirCompareTestCase.dir, ['file'], shallow=False) == (['file'], [], []), 'Comparing directory to itDirCompareTestCase fails')
    DirCompareTestCase.assertTrue(filecmp.cmpfiles(DirCompareTestCase.dir, DirCompareTestCase.dir_same, ['file'], shallow=False), 'Comparing directory to same fails')
    with open(os.path.join(DirCompareTestCase.dir, 'file2'), 'w') as output:
        output.write('Different contents.\n')
    DirCompareTestCase.assertFalse(filecmp.cmpfiles(DirCompareTestCase.dir, DirCompareTestCase.dir_same, ['file', 'file2']) == (['file'], ['file2'], []), 'Comparing mismatched directories fails')

DirCompareTestCase = test_filecmp.DirCompareTestCase()
DirCompareTestCase.setUp()
test_cmpfiles()
