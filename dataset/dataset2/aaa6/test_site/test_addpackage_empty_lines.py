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

def test_addpackage_empty_lines():
    (pth_dir, pth_fn) = HelperFunctionsTests.make_pth('\n\n  \n\n')
    known_paths = site.addpackage(pth_dir, pth_fn, set())
    HelperFunctionsTests.assertEqual(known_paths, set())

HelperFunctionsTests = test_site.HelperFunctionsTests()
test_addpackage_empty_lines()
