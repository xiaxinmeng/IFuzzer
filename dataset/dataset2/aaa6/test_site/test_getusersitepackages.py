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
def test_getusersitepackages():
    site.USER_SITE = None
    site.USER_BASE = None
    user_site = site.getusersitepackages()
    HelperFunctionsTests.assertEqual(site.USER_SITE, user_site)
    HelperFunctionsTests.assertTrue(user_site.startswith(site.USER_BASE), user_site)
    HelperFunctionsTests.assertEqual(site.USER_BASE, site.getuserbase())

HelperFunctionsTests = test_site.HelperFunctionsTests()
test_getusersitepackages()
