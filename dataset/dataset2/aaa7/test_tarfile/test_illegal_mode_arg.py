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

def test_illegal_mode_arg():
    with open(test_tarfile.tmpname, 'wb'):
        pass
    with MiscReadTestBase.assertRaisesRegex(ValueError, 'mode must be '):
        tar = MiscReadTestBase.taropen(test_tarfile.tmpname, 'q')
    with MiscReadTestBase.assertRaisesRegex(ValueError, 'mode must be '):
        tar = MiscReadTestBase.taropen(test_tarfile.tmpname, 'rw')
    with MiscReadTestBase.assertRaisesRegex(ValueError, 'mode must be '):
        tar = MiscReadTestBase.taropen(test_tarfile.tmpname, '')

MiscReadTestBase = test_tarfile.MiscReadTestBase()
test_illegal_mode_arg()
