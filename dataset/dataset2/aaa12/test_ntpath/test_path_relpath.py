import ntpath
import os
import sys
import unittest
import warnings
from test.support import os_helper
from test.support import TestFailed
from test.support.os_helper import FakePath
from test import test_genericpath
from tempfile import TemporaryFile

import ctypes
import test_ntpath

def test_path_relpath():
    PathLikeTests._check_function(PathLikeTests.path.relpath)

PathLikeTests = test_ntpath.PathLikeTests()
PathLikeTests.setUp()
test_path_relpath()
