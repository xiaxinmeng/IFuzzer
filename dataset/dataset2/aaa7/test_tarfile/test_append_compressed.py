import sys
import os
import io
from hashlib import sha256
from contextlib import contextmanager
from random import Random
import pathlib
import unittest
import unittest.mock
import tarfile
from test import support
from test.support import os_helper
from test.support import script_helper
import gzip

import pwd, grp
import test_tarfile

def test_append_compressed():
    AppendTestBase._create_testtar('w:' + AppendTestBase.suffix)
    AppendTestBase.assertRaises(tarfile.ReadError, tarfile.open, tmpname, 'a')

AppendTestBase = test_tarfile.AppendTestBase()
test_append_compressed()
