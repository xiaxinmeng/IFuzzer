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

def test_add_twice():
    tarinfo = HardlinkTest.tar.gettarinfo(HardlinkTest.foo)
    HardlinkTest.assertEqual(tarinfo.type, tarfile.REGTYPE, 'add file as regular failed')

HardlinkTest = test_tarfile.HardlinkTest()
test_add_twice()
