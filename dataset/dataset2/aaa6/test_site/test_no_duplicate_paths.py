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

def test_no_duplicate_paths():
    site.removeduppaths()
    seen_paths = set()
    for path in sys.path:
        ImportSideEffectTests.assertNotIn(path, seen_paths)
        seen_paths.add(path)

ImportSideEffectTests = test_site.ImportSideEffectTests()
test_no_duplicate_paths()
