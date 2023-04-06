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

def test_provoke_stream_error():
    tarinfos = StreamReadTest.tar.getmembers()
    with StreamReadTest.tar.extractfile(tarinfos[0]) as f:
        StreamReadTest.assertRaises(tarfile.StreamError, f.read)

StreamReadTest = test_tarfile.StreamReadTest()
StreamReadTest.setUp()
test_provoke_stream_error()
