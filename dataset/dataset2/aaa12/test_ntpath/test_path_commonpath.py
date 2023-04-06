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

def test_path_commonpath():
    common_path = PathLikeTests.path.commonpath([PathLikeTests.file_path, PathLikeTests.file_name])
    PathLikeTests.assertPathEqual(common_path, PathLikeTests.file_name)

PathLikeTests = test_ntpath.PathLikeTests()
PathLikeTests.setUp()
test_path_commonpath()
