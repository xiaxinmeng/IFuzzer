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

def test_check_members():
    for tarinfo in MiscReadTestBase.tar:
        MiscReadTestBase.assertEqual(int(tarinfo.mtime), 1041808783, 'wrong mtime for %s' % tarinfo.name)
        if not tarinfo.name.startswith('ustar/'):
            continue
        MiscReadTestBase.assertEqual(tarinfo.uname, 'tarfile', 'wrong uname for %s' % tarinfo.name)

MiscReadTestBase = test_tarfile.MiscReadTestBase()
test_check_members()
