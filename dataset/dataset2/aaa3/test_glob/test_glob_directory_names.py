import glob
import os
import shutil
import sys
import unittest
from test.support.os_helper import TESTFN, skip_unless_symlink, can_symlink, create_empty_file, change_cwd
import test_glob

def test_glob_directory_names():
    eq = GlobTests.assertSequencesEqual_noorder
    eq(GlobTests.glob('*', 'D'), [GlobTests.norm('a', 'D')])
    eq(GlobTests.glob('*', '*a'), [])
    eq(GlobTests.glob('a', '*', '*', '*a'), [GlobTests.norm('a', 'bcd', 'efg', 'ha')])
    eq(GlobTests.glob('?a?', '*F'), [GlobTests.norm('aaa', 'zzzF'), GlobTests.norm('aab', 'F')])

GlobTests = test_glob.GlobTests()
GlobTests.setUp()
test_glob_directory_names()
