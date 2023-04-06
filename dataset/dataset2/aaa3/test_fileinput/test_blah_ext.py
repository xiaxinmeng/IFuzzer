import os
import sys
import re
import fileinput
import collections
import builtins
import tempfile
import unittest

import gzip
from io import BytesIO, StringIO
from fileinput import FileInput, hook_encoded
from pathlib import Path
from test.support import verbose
from test.support.os_helper import TESTFN
from test.support.os_helper import unlink as safe_unlink
from test.support import os_helper
from test.support import warnings_helper
from test import support
from unittest import mock
import test_fileinput

def test_blah_ext():
    Test_hook_compressed.do_test_use_builtin_open('abcd.blah', 5)

Test_hook_compressed = test_fileinput.Test_hook_compressed()
Test_hook_compressed.setUp()
test_blah_ext()
