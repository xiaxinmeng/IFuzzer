import os
import sys
import re
import fileinput
import collections
import builtins
import tempfile
import unittest
import bz2
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

@unittest.skipUnless(bz2, 'Requires bz2')
def test_bz2_ext_fake():
    original_open = bz2.BZ2File
    bz2.BZ2File = Test_hook_compressed.fake_open
    try:
        result = fileinput.hook_compressed('test.bz2', 4)
    finally:
        bz2.BZ2File = original_open
    Test_hook_compressed.assertEqual(Test_hook_compressed.fake_open.invocation_count, 1)
    Test_hook_compressed.assertEqual(Test_hook_compressed.fake_open.last_invocation, (('test.bz2', 4), {}))

Test_hook_compressed = test_fileinput.Test_hook_compressed()
test_bz2_ext_fake()
