import glob
import os
import shutil
import sys
import unittest
from test.support.os_helper import TESTFN, skip_unless_symlink, can_symlink, create_empty_file, change_cwd
import test_glob

def test_escape():
    check = GlobTests.check_escape
    check('abc', 'abc')
    check('[', '[[]')
    check('?', '[?]')
    check('*', '[*]')
    check('[[_/*?*/_]]', '[[][[]_/[*][?][*]/_]]')
    check('/[[_/*?*/_]]/', '/[[][[]_/[*][?][*]/_]]/')

GlobTests = test_glob.GlobTests()
test_escape()
