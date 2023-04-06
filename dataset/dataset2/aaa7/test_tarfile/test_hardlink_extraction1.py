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

@unittest.skipIf(hasattr(os.path, 'islink'), 'Skip emulation - has os.path.islink but not os.link')
def test_hardlink_extraction1():
    LinkEmulationTest._test_link_extraction('ustar/lnktype')

LinkEmulationTest = test_tarfile.LinkEmulationTest()
test_hardlink_extraction1()
