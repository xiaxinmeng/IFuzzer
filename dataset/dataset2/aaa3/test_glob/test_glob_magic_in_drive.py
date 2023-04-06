import glob
import os
import shutil
import sys
import unittest
from test.support.os_helper import TESTFN, skip_unless_symlink, can_symlink, create_empty_file, change_cwd
import test_glob

@unittest.skipUnless(sys.platform == 'win32', 'Win32 specific test')
def test_glob_magic_in_drive():
    eq = GlobTests.assertSequencesEqual_noorder
    eq(glob.glob('*:'), [])
    eq(glob.glob(b'*:'), [])
    eq(glob.glob('?:'), [])
    eq(glob.glob(b'?:'), [])
    eq(glob.glob('\\\\?\\c:\\'), ['\\\\?\\c:\\'])
    eq(glob.glob(b'\\\\?\\c:\\'), [b'\\\\?\\c:\\'])
    eq(glob.glob('\\\\*\\*\\'), [])
    eq(glob.glob(b'\\\\*\\*\\'), [])

GlobTests = test_glob.GlobTests()
GlobTests.setUp()
test_glob_magic_in_drive()
