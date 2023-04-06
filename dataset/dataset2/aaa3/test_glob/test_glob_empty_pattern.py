import glob
import os
import shutil
import sys
import unittest
from test.support.os_helper import TESTFN, skip_unless_symlink, can_symlink, create_empty_file, change_cwd
import test_glob

def test_glob_empty_pattern():
    GlobTests.assertEqual(glob.glob(''), [])
    GlobTests.assertEqual(glob.glob(b''), [])
    GlobTests.assertEqual(glob.glob('', root_dir=GlobTests.tempdir), [])
    GlobTests.assertEqual(glob.glob(b'', root_dir=os.fsencode(GlobTests.tempdir)), [])
    GlobTests.assertEqual(glob.glob('', dir_fd=GlobTests.dir_fd), [])
    GlobTests.assertEqual(glob.glob(b'', dir_fd=GlobTests.dir_fd), [])

GlobTests = test_glob.GlobTests()
GlobTests.setUp()
test_glob_empty_pattern()
