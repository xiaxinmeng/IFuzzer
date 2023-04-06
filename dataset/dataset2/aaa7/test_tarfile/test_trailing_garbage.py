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

def test_trailing_garbage():
    data = tarfile.TarInfo('foo').tobuf()
    AppendTest._test_error(data + b'\x00' * 13)

AppendTest = test_tarfile.AppendTest()
AppendTest.setUp()
test_trailing_garbage()
