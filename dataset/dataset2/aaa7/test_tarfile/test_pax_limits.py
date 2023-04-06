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

def test_pax_limits():
    tarinfo = tarfile.TarInfo('123/' * 126 + 'longname')
    tarinfo.tobuf(tarfile.PAX_FORMAT)
    tarinfo = tarfile.TarInfo('longlink')
    tarinfo.linkname = '123/' * 126 + 'longname'
    tarinfo.tobuf(tarfile.PAX_FORMAT)
    tarinfo = tarfile.TarInfo('name')
    tarinfo.uid = 72057594037927936
    tarinfo.tobuf(tarfile.PAX_FORMAT)

LimitsTest = test_tarfile.LimitsTest()
test_pax_limits()
