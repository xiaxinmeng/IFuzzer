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

def test_premature_eof():
    data = tarfile.TarInfo('foo').tobuf()
    AppendTest._test_error(data)

AppendTest = test_tarfile.AppendTest()
AppendTest.setUp()
test_premature_eof()
