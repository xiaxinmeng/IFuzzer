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

def test_v7_dirtype():
    tarinfo = MiscReadTestBase.tar.getmember('misc/dirtype-old-v7')
    MiscReadTestBase.assertEqual(tarinfo.type, tarfile.DIRTYPE, 'v7 dirtype failed')

MiscReadTestBase = test_tarfile.MiscReadTestBase()
test_v7_dirtype()
