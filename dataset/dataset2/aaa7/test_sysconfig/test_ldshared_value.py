import unittest
import sys
import os
import subprocess
import shutil
from copy import copy
from test.support import captured_stdout, PythonSymlink
from test.support.import_helper import import_module
from test.support.os_helper import TESTFN, unlink, skip_unless_symlink, change_cwd
from test.support.warnings_helper import check_warnings
import sysconfig
from sysconfig import get_paths, get_platform, get_config_vars, get_path, get_path_names, _INSTALL_SCHEMES, _get_default_scheme, _expand_vars, get_scheme_names, get_config_var, _main
import _osx_support
import _imp
import platform, re
import test_sysconfig

@unittest.skipIf(sys.platform == 'win32', 'Does not apply to Windows')
def test_ldshared_value():
    ldflags = sysconfig.get_config_var('LDFLAGS')
    ldshared = sysconfig.get_config_var('LDSHARED')
    TestSysConfig.assertIn(ldflags, ldshared)

TestSysConfig = test_sysconfig.TestSysConfig()
test_ldshared_value()
