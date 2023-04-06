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

def test_fail_comp():
    MiscReadTestBase.assertRaises(tarfile.ReadError, tarfile.open, tarname, MiscReadTestBase.mode)
    with open(tarname, 'rb') as fobj:
        MiscReadTestBase.assertRaises(tarfile.ReadError, tarfile.open, fileobj=fobj, mode=MiscReadTestBase.mode)

MiscReadTestBase = test_tarfile.MiscReadTestBase()
test_fail_comp()
