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

@unittest.skipUnless(gzip, 'Requires gzip and zlib')
def test_gz_ext_fake():
    original_open = gzip.open
    gzip.open = Test_hook_compressed.fake_open
    try:
        result = fileinput.hook_compressed('test.gz', 3)
    finally:
        gzip.open = original_open
    Test_hook_compressed.assertEqual(Test_hook_compressed.fake_open.invocation_count, 1)
    Test_hook_compressed.assertEqual(Test_hook_compressed.fake_open.last_invocation, (('test.gz', 3), {}))

Test_hook_compressed = test_fileinput.Test_hook_compressed()
Test_hook_compressed.setUp()
test_gz_ext_fake()
