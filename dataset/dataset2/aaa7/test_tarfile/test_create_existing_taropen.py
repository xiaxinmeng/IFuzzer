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

def test_create_existing_taropen():
    with CreateTest.taropen(test_tarfile.tmpname, 'x') as tobj:
        tobj.add(CreateTest.file_path)
    with CreateTest.assertRaises(FileExistsError):
        with CreateTest.taropen(test_tarfile.tmpname, 'x'):
            pass
    with CreateTest.taropen(test_tarfile.tmpname) as tobj:
        names = tobj.getnames()
    CreateTest.assertEqual(len(names), 1)
    CreateTest.assertIn('spameggs42', names[0])

CreateTest = test_tarfile.CreateTest()
test_create_existing_taropen()