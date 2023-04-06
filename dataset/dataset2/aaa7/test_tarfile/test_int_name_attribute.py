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

def test_int_name_attribute():
    fd = os.open(MiscReadTestBase.tarname, os.O_RDONLY)
    with open(fd, 'rb') as fobj:
        MiscReadTestBase.assertIsInstance(fobj.name, int)
        with tarfile.open(fileobj=fobj, mode=MiscReadTestBase.mode) as tar:
            MiscReadTestBase.assertIsNone(tar.name)

MiscReadTestBase = test_tarfile.MiscReadTestBase()
test_int_name_attribute()
