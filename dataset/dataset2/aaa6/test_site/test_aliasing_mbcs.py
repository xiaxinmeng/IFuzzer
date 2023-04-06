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

def test_aliasing_mbcs():
    if sys.platform == 'win32':
        import locale
        if locale.getdefaultlocale()[1].startswith('cp'):
            for value in encodings.aliases.aliases.values():
                if value == 'mbcs':
                    break
            else:
                ImportSideEffectTests.fail('did not alias mbcs')

ImportSideEffectTests = test_site.ImportSideEffectTests()
test_aliasing_mbcs()
