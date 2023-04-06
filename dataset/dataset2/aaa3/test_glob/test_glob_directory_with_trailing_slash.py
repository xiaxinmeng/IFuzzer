import glob
import os
import shutil
import sys
import unittest
from test.support.os_helper import TESTFN, skip_unless_symlink, can_symlink, create_empty_file, change_cwd
import test_glob

def test_glob_directory_with_trailing_slash():
    res = glob.glob(GlobTests.norm('Z*Z') + os.sep)
    GlobTests.assertEqual(res, [])
    res = glob.glob(GlobTests.norm('ZZZ') + os.sep)
    GlobTests.assertEqual(res, [])
    res = glob.glob(GlobTests.norm('aa*') + os.sep)
    GlobTests.assertEqual(len(res), 2)
    GlobTests.assertIn(set(res), [{GlobTests.norm('aaa'), GlobTests.norm('aab')}, {GlobTests.norm('aaa') + os.sep, GlobTests.norm('aab') + os.sep}])

GlobTests = test_glob.GlobTests()
GlobTests.setUp()
test_glob_directory_with_trailing_slash()
