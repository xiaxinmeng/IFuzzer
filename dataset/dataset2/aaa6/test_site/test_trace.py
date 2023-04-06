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

def test_trace():
    message = 'bla-bla-bla'
    for (verbose, out) in ((True, message + '\n'), (False, '')):
        with mock.patch('sys.flags', mock.Mock(verbose=verbose)), mock.patch('sys.stderr', io.StringIO()):
            site._trace(message)
            HelperFunctionsTests.assertEqual(sys.stderr.getvalue(), out)

HelperFunctionsTests = test_site.HelperFunctionsTests()
test_trace()
