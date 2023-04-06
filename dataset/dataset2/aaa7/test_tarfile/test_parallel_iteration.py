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

def test_parallel_iteration():
    with tarfile.open(MiscReadTestBase.tarname) as tar:
        for (m1, m2) in zip(tar, tar):
            MiscReadTestBase.assertEqual(m1.offset, m2.offset)
            MiscReadTestBase.assertEqual(m1.get_info(), m2.get_info())

MiscReadTestBase = test_tarfile.MiscReadTestBase()
test_parallel_iteration()
