import glob
import os
import shutil
import sys
import unittest
from test.support.os_helper import TESTFN, skip_unless_symlink, can_symlink, create_empty_file, change_cwd
import test_glob

@unittest.skipUnless(sys.platform == 'win32', 'Win32 specific test')
def test_escape_windows():
    check = GlobTests.check_escape
    check('?:?', '?:[?]')
    check('*:*', '*:[*]')
    check('\\\\?\\c:\\?', '\\\\?\\c:\\[?]')
    check('\\\\*\\*\\*', '\\\\*\\*\\[*]')
    check('//?/c:/?', '//?/c:/[?]')
    check('//*/*/*', '//*/*/[*]')

GlobTests = test_glob.GlobTests()
test_escape_windows()
