import glob
import os
import shutil
import sys
import unittest
from test.support.os_helper import TESTFN, skip_unless_symlink, can_symlink, create_empty_file, change_cwd
import test_glob

def test_glob_nested_directory():
    eq = GlobTests.assertSequencesEqual_noorder
    if os.path.normcase('abCD') == 'abCD':
        eq(GlobTests.glob('a', 'bcd', 'E*'), [GlobTests.norm('a', 'bcd', 'EF')])
    else:
        eq(GlobTests.glob('a', 'bcd', 'E*'), [GlobTests.norm('a', 'bcd', 'EF'), GlobTests.norm('a', 'bcd', 'efg')])
    eq(GlobTests.glob('a', 'bcd', '*g'), [GlobTests.norm('a', 'bcd', 'efg')])

GlobTests = test_glob.GlobTests()
GlobTests.setUp()
test_glob_nested_directory()
