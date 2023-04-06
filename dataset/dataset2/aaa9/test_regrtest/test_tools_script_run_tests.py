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

@unittest.skipUnless(sysconfig.is_python_build(), 'run_tests.py script is not installed')
def test_tools_script_run_tests():
    script = os.path.join(test_regrtest.ROOT_DIR, 'Tools', 'scripts', 'run_tests.py')
    args = [script, *ProgramsTestCase.regrtest_args, *ProgramsTestCase.tests]
    ProgramsTestCase.run_tests(args)

ProgramsTestCase = test_regrtest.ProgramsTestCase()
ProgramsTestCase.setUp()
test_tools_script_run_tests()
