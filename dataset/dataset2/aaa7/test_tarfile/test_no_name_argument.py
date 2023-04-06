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

def test_no_name_argument():
    MiscReadTestBase.requires_name_attribute()
    with open(MiscReadTestBase.tarname, 'rb') as fobj:
        MiscReadTestBase.assertIsInstance(fobj.name, str)
        with tarfile.open(fileobj=fobj, mode=MiscReadTestBase.mode) as tar:
            MiscReadTestBase.assertIsInstance(tar.name, str)
            MiscReadTestBase.assertEqual(tar.name, os.path.abspath(fobj.name))

MiscReadTestBase = test_tarfile.MiscReadTestBase()
test_no_name_argument()
