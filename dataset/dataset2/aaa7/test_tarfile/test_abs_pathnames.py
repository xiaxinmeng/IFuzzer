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

def test_abs_pathnames():
    if sys.platform == 'win32':
        WriteTest._test_pathname('C:\\foo', 'foo')
    else:
        WriteTest._test_pathname('/foo', 'foo')
        WriteTest._test_pathname('///foo', 'foo')

WriteTest = test_tarfile.WriteTest()
test_abs_pathnames()
