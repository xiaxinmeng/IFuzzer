import glob
import os
import shutil
import sys
import unittest
from test.support.os_helper import TESTFN, skip_unless_symlink, can_symlink, create_empty_file, change_cwd
import test_glob

def test_glob_one_directory():
    eq = GlobTests.assertSequencesEqual_noorder
    eq(GlobTests.glob('a*'), map(GlobTests.norm, ['a', 'aab', 'aaa']))
    eq(GlobTests.glob('*a'), map(GlobTests.norm, ['a', 'aaa']))
    eq(GlobTests.glob('.*'), map(GlobTests.norm, ['.aa', '.bb']))
    eq(GlobTests.glob('?aa'), map(GlobTests.norm, ['aaa']))
    eq(GlobTests.glob('aa?'), map(GlobTests.norm, ['aaa', 'aab']))
    eq(GlobTests.glob('aa[ab]'), map(GlobTests.norm, ['aaa', 'aab']))
    eq(GlobTests.glob('*q'), [])

GlobTests = test_glob.GlobTests()
GlobTests.setUp()
test_glob_one_directory()
