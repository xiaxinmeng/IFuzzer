import filecmp
import os
import shutil
import tempfile
import unittest
from test import support
from test.support import os_helper
import test_filecmp

def test_different():
    FileCompareTestCase.assertFalse(filecmp.cmp(FileCompareTestCase.name, FileCompareTestCase.name_diff), 'Mismatched files compare as equal')
    FileCompareTestCase.assertFalse(filecmp.cmp(FileCompareTestCase.name, FileCompareTestCase.dir), 'File and directory compare as equal')

FileCompareTestCase = test_filecmp.FileCompareTestCase()
FileCompareTestCase.setUp()
test_different()
