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

def test_sparse_file_10():
    GNUReadTest._test_sparse_file('gnu/sparse-1.0')

GNUReadTest = test_tarfile.GNUReadTest()
GNUReadTest.setUp()
test_sparse_file_10()
