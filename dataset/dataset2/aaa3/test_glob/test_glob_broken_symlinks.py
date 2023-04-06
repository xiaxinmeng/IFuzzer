import glob
import os
import shutil
import sys
import unittest
from test.support.os_helper import TESTFN, skip_unless_symlink, can_symlink, create_empty_file, change_cwd
import test_glob

@skip_unless_symlink
def test_glob_broken_symlinks():
    eq = GlobTests.assertSequencesEqual_noorder
    eq(GlobTests.glob('sym*'), [GlobTests.norm('sym1'), GlobTests.norm('sym2'), GlobTests.norm('sym3')])
    eq(GlobTests.glob('sym1'), [GlobTests.norm('sym1')])
    eq(GlobTests.glob('sym2'), [GlobTests.norm('sym2')])

GlobTests = test_glob.GlobTests()
GlobTests.setUp()
test_glob_broken_symlinks()
