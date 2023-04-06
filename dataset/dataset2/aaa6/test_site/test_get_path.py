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

@unittest.skipUnless(test_site.HAS_USER_SITE, 'need user site')
def test_get_path():
    if sys.platform == 'darwin' and sys._framework:
        scheme = 'osx_framework_user'
    else:
        scheme = os.name + '_user'
    HelperFunctionsTests.assertEqual(site._get_path(site._getuserbase()), sysconfig.get_path('purelib', scheme))

HelperFunctionsTests = test_site.HelperFunctionsTests()
test_get_path()
