import filecmp
import os
import shutil
import tempfile
import unittest
from test import support
from test.support import os_helper
import test_filecmp

def test_matching():
    FileCompareTestCase.assertTrue(filecmp.cmp(FileCompareTestCase.name, FileCompareTestCase.name), 'Comparing file to itFileCompareTestCase fails')
    FileCompareTestCase.assertTrue(filecmp.cmp(FileCompareTestCase.name, FileCompareTestCase.name, shallow=False), 'Comparing file to itFileCompareTestCase fails')
    FileCompareTestCase.assertTrue(filecmp.cmp(FileCompareTestCase.name, FileCompareTestCase.name_same), 'Comparing file to identical file fails')
    FileCompareTestCase.assertTrue(filecmp.cmp(FileCompareTestCase.name, FileCompareTestCase.name_same, shallow=False), 'Comparing file to identical file fails')

FileCompareTestCase = test_filecmp.FileCompareTestCase()
FileCompareTestCase.setUp()
test_matching()
