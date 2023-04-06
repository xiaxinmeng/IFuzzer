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

def test_xstar_type():
    try:
        MiscReadTestBase.tar.getmember('misc/regtype-xstar')
    except KeyError:
        MiscReadTestBase.fail('failed to find misc/regtype-xstar (mangled prefix?)')

MiscReadTestBase = test_tarfile.MiscReadTestBase()
test_xstar_type()
