import unittest
import test.support
from test import support
from test.support import os_helper
from test.support import socket_helper
from test.support import captured_stderr
from test.support.os_helper import TESTFN, EnvironmentVarGuard, change_cwd
import builtins
import encodings
import glob
import io
import os
import re
import shutil
import subprocess
import sys
import sysconfig
import tempfile
import urllib.error
import urllib.request
from unittest import mock
from copy import copy
import site
import sysconfig
import locale

import test_site

def test_addsitedir():
    pth_file = test_site.PthFile()
    pth_file.cleanup(prep=True)
    try:
        pth_file.create()
        site.addsitedir(pth_file.base_dir, set())
        HelperFunctionsTests.pth_file_tests(pth_file)
    finally:
        pth_file.cleanup()

HelperFunctionsTests = test_site.HelperFunctionsTests()
test_addsitedir()
