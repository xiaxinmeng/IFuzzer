import glob
import os
import shutil
import sys
import unittest
from test.support.os_helper import TESTFN, skip_unless_symlink, can_symlink, create_empty_file, change_cwd
import test_glob

@skip_unless_symlink
def test_glob_symlinks():
    eq = GlobTests.assertSequencesEqual_noorder
    eq(GlobTests.glob('sym3'), [GlobTests.norm('sym3')])
    eq(GlobTests.glob('sym3', '*'), [GlobTests.norm('sym3', 'EF'), GlobTests.norm('sym3', 'efg')])
    GlobTests.assertIn(GlobTests.glob('sym3' + os.sep), [[GlobTests.norm('sym3')], [GlobTests.norm('sym3') + os.sep]])
    eq(GlobTests.glob('*', '*F'), [GlobTests.norm('aaa', 'zzzF'), GlobTests.norm('aab', 'F'), GlobTests.norm('sym3', 'EF')])

GlobTests = test_glob.GlobTests()
GlobTests.setUp()
test_glob_symlinks()
