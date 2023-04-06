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

def test_read_through():
    for tarinfo in StreamReadTest.tar:
        if not tarinfo.isreg():
            continue
        with StreamReadTest.tar.extractfile(tarinfo) as fobj:
            while True:
                try:
                    buf = fobj.read(512)
                except tarfile.StreamError:
                    StreamReadTest.fail('simple read-through using TarFile.extractfile() failed')
                if not buf:
                    break

StreamReadTest = test_tarfile.StreamReadTest()
StreamReadTest.setUp()
test_read_through()
