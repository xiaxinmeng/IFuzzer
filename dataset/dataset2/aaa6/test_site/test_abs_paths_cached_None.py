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

def test_abs_paths_cached_None():
    """Test for __cached__ is None.

        Regarding to PEP 3147, __cached__ can be None.

        See also: https://bugs.python.org/issue30167
        """
    sys.modules['test'].__cached__ = None
    site.abs_paths()
    ImportSideEffectTests.assertIsNone(sys.modules['test'].__cached__)

ImportSideEffectTests = test_site.ImportSideEffectTests()
test_abs_paths_cached_None()
