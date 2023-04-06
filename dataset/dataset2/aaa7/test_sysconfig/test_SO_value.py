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

@unittest.skipIf(sysconfig.get_config_var('EXT_SUFFIX') is None, 'EXT_SUFFIX required for this test')
def test_SO_value():
    with check_warnings(('', DeprecationWarning)):
        TestSysConfig.assertEqual(sysconfig.get_config_var('SO'), sysconfig.get_config_var('EXT_SUFFIX'))

TestSysConfig = test_sysconfig.TestSysConfig()
test_SO_value()
