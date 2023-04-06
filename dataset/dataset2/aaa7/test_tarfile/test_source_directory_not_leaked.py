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

def test_source_directory_not_leaked():
    """
        Ensure the source directory is not included in the tar header
        per bpo-41316.
        """
    tarfile.open(test_tarfile.tmpname, GzipStreamWriteTest.mode).close()
    payload = pathlib.Path(test_tarfile.tmpname).read_text(encoding='latin-1')
    assert os.path.dirname(test_tarfile.tmpname) not in payload

GzipStreamWriteTest = test_tarfile.GzipStreamWriteTest()
test_source_directory_not_leaked()
