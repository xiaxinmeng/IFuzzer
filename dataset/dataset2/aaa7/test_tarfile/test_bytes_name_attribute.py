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

def test_bytes_name_attribute():
    MiscReadTestBase.requires_name_attribute()
    tarname = os.fsencode(MiscReadTestBase.tarname)
    with open(tarname, 'rb') as fobj:
        MiscReadTestBase.assertIsInstance(fobj.name, bytes)
        with tarfile.open(fileobj=fobj, mode=MiscReadTestBase.mode) as tar:
            MiscReadTestBase.assertIsInstance(tar.name, bytes)
            MiscReadTestBase.assertEqual(tar.name, os.path.abspath(fobj.name))

MiscReadTestBase = test_tarfile.MiscReadTestBase()
MiscReadTestBase.setUp()
test_bytes_name_attribute()
