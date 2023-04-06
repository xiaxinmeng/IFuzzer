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

def test_script_autotest():
    script = os.path.join(ProgramsTestCase.testdir, 'autotest.py')
    args = [*ProgramsTestCase.python_args, script, *ProgramsTestCase.regrtest_args, *ProgramsTestCase.tests]
    ProgramsTestCase.run_tests(args)

ProgramsTestCase = test_regrtest.ProgramsTestCase()
ProgramsTestCase.setUp()
test_script_autotest()
