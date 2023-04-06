import filecmp
import os
import shutil
import tempfile
import unittest
from test import support
from test.support import os_helper
import test_filecmp

def test_default_ignores():
    DirCompareTestCase.assertIn('.hg', filecmp.DEFAULT_IGNORES)

DirCompareTestCase = test_filecmp.DirCompareTestCase()
test_default_ignores()
