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

def test_existing():
    AppendTest._create_testtar()
    AppendTest._add_testfile()
    AppendTest._test(names=['foo', 'bar'])

AppendTest = test_tarfile.AppendTest()
AppendTest.setUp()
test_existing()
