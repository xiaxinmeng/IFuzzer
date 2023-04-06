import contextlib
import glob
import io
import os.path
import platform
import re
import subprocess
import sys
import sysconfig
import tempfile
import textwrap
import unittest
from test import libregrtest
from test import support
from test.support import os_helper
from test.libregrtest import utils
import test_regrtest

@unittest.skipUnless(sysconfig.is_python_build(), 'test.bat script is not installed')
@unittest.skipUnless(sys.platform == 'win32', 'Windows only')
def test_tools_buildbot_test():
    script = os.path.join(ROOT_DIR, 'Tools', 'buildbot', 'test.bat')
    test_args = ['--testdir=%s' % ProgramsTestCase.tmptestdir]
    if platform.machine() == 'ARM64':
        test_args.append('-arm64')
    elif platform.machine() == 'ARM':
        test_args.append('-arm32')
    elif platform.architecture()[0] == '64bit':
        test_args.append('-x64')
    if not Py_DEBUG:
        test_args.append('+d')
    ProgramsTestCase.run_batch(script, *test_args, *ProgramsTestCase.tests)

ProgramsTestCase = test_regrtest.ProgramsTestCase()
test_tools_buildbot_test()
